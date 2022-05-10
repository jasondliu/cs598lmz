import mmap
import re
import sys
import time
import traceback

from . import config
from . import utils
from . import __version__

# -----------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------

# The maximum number of bytes to read from a file at a time.
MAX_READ_SIZE = 2**20

# The maximum number of bytes to read from a file at a time when doing a
# binary search.
MAX_BINARY_READ_SIZE = 2**16

# The number of bytes to read from a file at a time when doing a binary search
# for a pattern.
BINARY_READ_SIZE = 2**14

# The number of bytes to read from a file at a time when doing a binary search
# for a pattern.
BINARY_READ_SIZE = 2**14

# The number of bytes to read from a file at a time when doing a binary search
# for a pattern.
BINARY_READ_SIZE = 2**14

# The number of bytes to read from a file at a time when doing a binary search
# for a pattern.
BINARY_
