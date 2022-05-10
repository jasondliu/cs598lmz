import mmap
import os
import sys
import time
import traceback

from . import file_util
from . import log
from . import util

# pylint: disable=too-many-lines

#
# Constants
#

# The maximum number of bytes to read from a file at a time.
_MAX_READ_SIZE = 1024 * 1024

# The maximum number of bytes to read from a file at a time when
# reading the file backwards.
_MAX_READ_BACKWARDS_SIZE = 1024 * 1024

# The maximum number of bytes to read from a file at a time when
# reading the file backwards.
_MAX_READ_BACKWARDS_SIZE = 1024 * 1024

# The maximum number of bytes to read from a file at a time when
# reading the file backwards.
_MAX_READ_BACKWARDS_SIZE = 1024 * 1024

# The maximum number of bytes to read from a file at a time when
# reading the file backwards.
_MAX_READ_BACKWARDS_SIZE = 1024 * 1024

# The maximum number of bytes to read from a file at a time when
