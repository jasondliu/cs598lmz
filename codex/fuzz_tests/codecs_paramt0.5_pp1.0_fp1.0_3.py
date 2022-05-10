import codecs
codecs.register_error('strict', codecs.ignore_errors)

import re
import logging

logger = logging.getLogger(__name__)

def get_config(path):
    """
    Returns a config object from a file.
    """
    return Config(path)


class Config(object):
    """
    Represents a configuration file
    """

    def __init__(self, path):
        """
        Constructor
        """
        self.path = path
        self.sections = []
        self.load()

    def load(self):
        """
        Loads the configuration file.
        """
        try:
            with open(self.path, 'r') as f:
                self.content = f.read()
        except IOError:
            self.content = ''

        self.sections = []
        section = None

        for line in self.content.splitlines():
            line = line.strip()

            if not line:
                continue

            if line.startswith('[') and line.endswith(']'):
                section = Section(
