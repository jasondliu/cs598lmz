import mmap
import os
import re
import sys
import time
import traceback

from lib import config
from lib import daemon
from lib import log
from lib import util

from lib.config import ConfigError

from lib.daemon import DaemonError

from lib.log import LogError

from lib.util import UtilError

#-------------------------------------------------------------------------------

#
# Class: FileMonitor
#
# Monitors one or more files for changes.
#
# Methods:
