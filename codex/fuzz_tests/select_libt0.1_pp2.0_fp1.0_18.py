import select
import socket
import sys
import threading
import time
import traceback

from . import common
from . import config
from . import constants
from . import errors
from . import log
from . import util
from . import version

# pylint: disable=too-many-lines

# pylint: disable=too-many-instance-attributes
class Server(object):
    """
    The main server class.
    """

    def __init__(self, config_file=None, config_dict=None, config_data=None,
                 config_path=None, config_base_dir=None, config_user_dir=None,
                 config_dirs=None, config_env_vars=None, config_args=None,
                 config_defaults=None, config_overrides=None,
                 config_allow_unknown=False, config_allow_missing=False,
                 config_allow_duplicates=False, config_allow_overrides=False,
                 config_allow_no_value=False, config_allow_empty_values=
