import mmap
import os
import re
import sys
import time

from collections import defaultdict
from datetime import datetime
from optparse import OptionParser

from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import get_lexer_by_name

from . import __version__
from . import config
from . import log
from . import utils
from . import xdg

#
# Globals
#

# Default configuration file
DEFAULT_CONFIG_FILE = os.path.join(xdg.XDG_CONFIG_HOME, 'logtop', 'logtop.conf')

# Default log file
DEFAULT_LOG_FILE = os.path.join(xdg.XDG_DATA_HOME, 'logtop', 'logtop.log')

# Default log level
DEFAULT_LOG_LEVEL = 'info'

# Default log format
DEFAULT_LOG_FORMAT = '%(asctime)s %(levelname)s %(message)s'

# Default log date format
DEFAULT_
