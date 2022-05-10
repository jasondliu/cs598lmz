import mmap
import os
import re
import subprocess
import sys
import tempfile
import time
import traceback

from . import config
from . import constants
from . import errors
from . import file_util
from . import log
from . import util
from . import version

# The maximum number of bytes to read from a file.
MAX_FILE_SIZE = 1024 * 1024

# The maximum number of bytes to read from a process's stdout/stderr.
MAX_PROCESS_OUTPUT = 1024 * 1024

# The maximum number of bytes to read from a process's stdout/stderr when
# running a command.
MAX_COMMAND_OUTPUT = 1024 * 1024

# The maximum number of bytes to read from a process's stdout/stderr when
# running a command.
MAX_COMMAND_OUTPUT = 1024 * 1024

# The maximum number of bytes to read from a process's stdout/stderr when
# running a command.
MAX_COMMAND_OUTPUT = 1024 * 1024

# The maximum number of bytes to read from
