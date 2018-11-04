import os
import yaml

from feeder.resource.ftp.validator import FTPConfigValidator
from feeder.resource.http.validator import HTTPConfigValidator
from feeder.parser.validator import ReadConfigValidator
from feeder.writer.validator import WriteConfigValidator

RESOURCE_VALIDATORS = {
    'ftp': FTPConfigValidator,
    'http': HTTPConfigValidator,
    'https': HTTPConfigValidator
}


class Manifest(object):

    def __init__(self, config_path):
        self.raw_data = yaml.load(file(config_path, 'r'))
        self.config = self.validate_manifest(config_path)

    def validate_manifest(self, config_path):
        conf = {}
        conf['source'] = self._validate_source_configuration()
        conf['read_manifest'] = self._validate_read_configuration()
        conf['write_manifest'] = self._validate_write_configurations()
        return conf

    def _validate_source_configuration(self):
        pass

    def _validate_read_configuration(self):
        pass

    def _validate_write_configurations(self):
        pass
