import mmap
import os
import re
import sys
import time

from . import __version__
from . import config
from . import db
from . import log
from . import util
from . import xdg

logger = log.get_logger(__name__)


def get_config_dir():
    """Return the configuration directory."""
    return xdg.get_config_dir('qutebrowser')


def get_config_file():
    """Return the config file path."""
    return os.path.join(get_config_dir(), 'config.py')


def get_config_py():
    """Get the config.py as a string."""
    try:
        with open(get_config_file(), 'r', encoding='utf-8') as f:
            return f.read()
    except OSError as e:
        if e.errno == errno.ENOENT:
            return ''
        else:
            raise


def get_config_py_autoconfig():
    """Get the autoconfig.yml as a
