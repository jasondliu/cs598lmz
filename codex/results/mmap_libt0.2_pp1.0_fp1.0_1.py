import mmap
import re
import sys
import time
import traceback

from . import config
from . import log
from . import util
from . import version
from . import xdg

# pylint: disable=too-many-lines

# -----------------------------------------------------------------------------

_logger = log.get_logger(__name__)

# -----------------------------------------------------------------------------

_DEFAULT_CONFIG_FILE = 'config.ini'

_DEFAULT_CONFIG_FILE_PATH = os.path.join(xdg.get_config_dir(), _DEFAULT_CONFIG_FILE)

_DEFAULT_CONFIG_FILE_CONTENT = '''\
[general]
# The default configuration file is located at {config_file_path}

# The default log file is located at {log_file_path}

# The default data directory is located at {data_dir_path}

# The default cache directory is located at {cache_dir_path}

# The default temporary directory is located at {temp_dir_path}

# The default configuration directory is located at {config_dir_
