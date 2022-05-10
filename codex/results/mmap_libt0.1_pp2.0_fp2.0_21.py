import mmap
import os
import re
import sys
import time
import traceback

from . import __version__
from . import config
from . import log
from . import util
from . import xdg

# -----------------------------------------------------------------------------
# Globals

_log = log.get_logger(__name__)

# -----------------------------------------------------------------------------
#

class Error(Exception):
    pass

# -----------------------------------------------------------------------------
#

class ConfigError(Error):
    pass

# -----------------------------------------------------------------------------
#

class Config(object):
    """
    Configuration object.
    """

    def __init__(self, config_file=None, config_dir=None, config_name=None,
                 config_ext=None, config_data=None, config_defaults=None,
                 config_env=None, config_env_prefix=None, config_env_sep=None,
                 config_env_strip=None, config_env_lower=None,
                 config_env_upper=None, config_env_bool=None,
                 config_env_int=None, config_env_float
