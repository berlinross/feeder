class BaseValidator(object):

    def __init__(self, configuration):
        self.errors = {}
        self.configuration = configuration

    def add_error(self, key, message):
        self.error[key] = message

    def validate(self):
        raise NotImplementedError(
            '`validate` must be implemented by the inheriting subclass'
        )


class SourceValidator(BaseValidator):

    ADDRESS_COMPONENTS = ['domain', 'path', 'params', 'auth']

    def _validate_ftp(self):
        return True, {}

    def _validate_http(self):
        method = self.configuration.get('method', None)
        address = self.configuration.get('address', {})

        if not method:
            self.add_error('method', 'Missing required method')

        if not address:
            self.add_error('address', 'Missing required address')

        components = address.get('components', {})
        if not components:
            self.add_error(
                'address.components', 'Address missing required components')

        component_keys = components.keys()
        if set(component_keys).difference(set(self.ADDRESS_COMPONENTS)):
            self.add_error(
                'address.components.keys',
                'Unrecognized address component keys added. Please revise.'
            )

        if self.errors:
            return False, self.errors

        return True, {}

    def validate(self):
        protocol = self.configuration.get('protocol', None)

        if not protocol:
            self.add_error('protocol', 'Missing protocol')
            return False, self.errors

        validator = getattr(self, protocol, None)
        if not validator:
            self.add_error(
                'validator',
                'No validator method matching protocol: {}'.format(protocol)
            )
            return False, self.errors

        return validator()


class ParserValidator(BaseValidator):

    def validate(self):
        data_points = self.configuration.get('datapoints', [])

        if not data_points:
            self.add_error('data', 'Data points not specified')
            return False, self.errors

        if not isinstance(data_points, (list, tuple)):
            self.add_error('data', 'Data points expected to be a list')
            return False, self.errors


class TransformerValidator(BaseValidator):

    def validate(self):
        return True, {}


class SaveValidator(BaseValidator):

    def validate(self):
        return True, {}
