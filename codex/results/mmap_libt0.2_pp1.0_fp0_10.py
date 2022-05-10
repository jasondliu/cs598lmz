import mmap
import os
import re
import sys
import time
import traceback

from . import config
from . import util
from . import version
from . import xlogging

_logger = xlogging.getLogger(__name__)

_g_config = config.load_config()
_g_config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json')

_g_config_file_lock = threading.Lock()
_g_config_file_lock.acquire()
_g_config_file_lock.release()


def _load_config():
    global _g_config
    _g_config = config.load_config()


def _save_config():
    global _g_config
    config.save_config(_g_config)


def _get_config():
    return _g_config


def _get_config_file():
    return _g_config_file


def _get_config_file_lock():
    return _g
