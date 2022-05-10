import mmap
import os
import re
import signal
import sys
import time
import traceback

from . import config
from . import log
from . import util
from . import version

# pylint: disable=too-many-lines

#
# Constants
#

#
# Globals
#

#
# Functions
#

def _get_pid_file_path():
    return os.path.join(config.get_config_dir(), 'pid')

def _get_pid():
    pid_file_path = _get_pid_file_path()
    if not os.path.exists(pid_file_path):
        return None

    with open(pid_file_path, 'r') as pid_file:
        pid = pid_file.read().strip()
        if not pid:
            return None

    return int(pid)

def _write_pid():
    pid_file_path = _get_pid_file_path()
    with open(pid_file_path, 'w') as pid_file:
        pid_file
