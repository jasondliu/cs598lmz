import mmap
import os
import re
import sys
import time
import traceback

from . import __version__
from . import config
from . import utils
from . import xdg

# -----------------------------------------------------------------------------
#
# Constants
#
# -----------------------------------------------------------------------------

# The default name of the configuration file.
DEFAULT_CONFIG_FILE = 'config.ini'

# The default name of the log file.
DEFAULT_LOG_FILE = 'log.txt'

# The default name of the PID file.
DEFAULT_PID_FILE = 'pid.txt'

# The default name of the socket file.
DEFAULT_SOCKET_FILE = 'socket.sock'

# The default name of the state file.
DEFAULT_STATE_FILE = 'state.json'

# The default name of the temporary file.
DEFAULT_TEMP_FILE = 'temp.txt'

# The default name of the temporary directory.
DEFAULT_TEMP_DIR = 'temp'

# The default name of the temporary directory.
DEFAULT_TEMP_DIR_2 = '
