import yaml

from feeder.validators import (
    SourceValidator,
    ParserValidator,
    TransformerValidator,
    SaveValidator
)


class Manifest(object):

    def __init__(self, config_path):
        self.raw_data = yaml.load(file(config_path, 'r'))
        self.save_manifest = self.raw_data.get('save', {})
        self.source_manifest = self.raw_data.get('source', {})
        self.parser_manifest = self.raw_data.get('response', {})
        self.transform_manifest = self.raw_data.get('transform', {})

    def validate_manifest(self):
        source_valid, source_erorrs = self._validate_source_configuration()
        if not source_valid:
            return source_erorrs

        parser_valid, parser_errors = self._validate_parse_configuration()
        if not parser_valid:
            return parser_errors

        tf_valid, tf_errors = self._validate_transform_configuration()
        if not tf_valid:
            return tf_errors

        save_valid, save_errors = self._validate_save_configuration()
        if not save_valid:
            return save_errors

    def _validate_source_configuration(self):
        return SourceValidator(self.source_manifest).validate()

    def _validate_parse_configuration(self):
        return ParserValidator(self.parser_manifest).validate()

    def _validate_transform_configuration(self):
        return TransformerValidator(self.transform_manifest).validate()

    def _validate_save_configuration(self):
        return SaveValidator(self.save_manifest).validate()
