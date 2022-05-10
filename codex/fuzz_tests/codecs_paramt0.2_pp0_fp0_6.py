import codecs
codecs.register_error('strict', codecs.ignore_errors)

from . import utils
from . import config
from . import logger
from . import exceptions
from . import __version__

__all__ = ['get_version', 'get_config', 'get_logger', 'get_exception', 'get_utils']

def get_version():
    return __version__

def get_config():
    return config

def get_logger():
    return logger

def get_exception():
    return exceptions

def get_utils():
    return utils
