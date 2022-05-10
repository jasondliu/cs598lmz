import mmap
import os
import sys
import time

from . import __version__
from . import config
from . import log
from . import util
from . import xdg

# The default config file.
DEFAULT_CONFIG_FILE = os.path.join(xdg.get_config_dir(), "pylog.conf")

# The default log file.
DEFAULT_LOG_FILE = os.path.join(xdg.get_data_dir(), "pylog.log")

# The default log format.
DEFAULT_LOG_FORMAT = "%(asctime)s %(levelname)s: %(message)s"

# The default log level.
DEFAULT_LOG_LEVEL = "INFO"

# The default log file mode.
DEFAULT_LOG_FILE_MODE = 0o600

# The default log file owner.
DEFAULT_LOG_FILE_OWNER = None

# The default log file group.
DEFAULT_LOG_FILE_GROUP = None

# The default log file rotation interval.
DEFAULT_LOG_FILE_R
