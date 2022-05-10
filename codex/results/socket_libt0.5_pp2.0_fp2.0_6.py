import socket
import urllib2
import StringIO
import ConfigParser
import os
import sys
import subprocess
import shutil
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)


def get_config_file():
    """
    Get the path to the configuration file.
    """
    if 'TEST_CONFIG_FILE' in os.environ:
        return os.environ['TEST_CONFIG_FILE']
    else:
        return os.path.join(os.path.dirname(__file__), 'config.ini')


def get_config():
    """
    Read the configuration file.
    """
    config_file = get_config_file()
    config = ConfigParser.ConfigParser()
    config.read(config_file)
    return config


def run_command(command, env=None, ignore_errors=False):
    """
    Run
