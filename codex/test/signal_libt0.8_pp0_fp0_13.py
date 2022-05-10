import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import time
import argparse
import logging
import numpy
import logging
import subprocess
import ujson
import json

# For python 2.7
try:
    import ConfigParser as configparser
except ImportError:
    import configparser

import pysftp

# Import our code.
import shuttlenet.shuttlenet_common
import shuttlenet.shuttlenet_db
import shuttlenet.shuttlenet_clients


db_logging = logging.getLogger('db')
camera_logging = logging.getLogger('camera')
client_logging = logging.getLogger('client')
card_logging = logging.getLogger('card')

def read_config(config_filename):
    """
    Reads a configuration file and returns a configuration object.
    """
    config = configparser.ConfigParser()
    config.read(config_filename)

    return config
