import weakref
import os
import sys
import time
import threading
import logging
import socket
import struct

from . import common
from . import config
from . import utils
from . import log

logger = logging.getLogger(__name__)

def _get_socket_name(socket_dir, socket_file):
    return os.path.join(socket_dir, socket_file)

def _get_socket_name_from_config(config):
    return _get_socket_name(config.socket_dir, config.socket_file)

def _get_socket_name_from_config_default(config):
    return _get_socket_name(config.socket_dir_default, config.socket_file_default)

def _get_socket_name_from_config_default_fallback(config):
    return _get_socket_name(config.socket_dir_default_fallback, config.socket_file_default_fallback)
