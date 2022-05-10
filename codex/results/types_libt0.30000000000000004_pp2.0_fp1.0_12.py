import types
types.ModuleType.__repr__ = lambda self: self.__name__

import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from unittest.mock import patch, Mock

from src.utils.config import Config
from src.utils.logger import Logger
from src.utils.exceptions import ConfigError

from src.utils.config import __CONFIG_FILE__

class TestConfig(unittest.TestCase):
    def setUp(self):
        self.config = Config()

    def test_config_init(self):
        self.assertEqual(self.config.config_file, __CONFIG_FILE__)
        self.assertEqual(self.config.config, {})
        self.assertEqual(self.config.logger, Logger())

    def test_config_init_with_config_file(self):
        config_file = 'config.json'
        config = Config(config_file)
       
