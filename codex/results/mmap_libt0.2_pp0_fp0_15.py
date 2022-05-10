import mmap
import os
import re
import sys
import time

from . import util
from . import version

# The default maximum number of bytes to read from a file.
DEFAULT_MAX_BYTES = 1024 * 1024

# The default maximum number of bytes to read from a file when using the
# --max-bytes-per-file option.
DEFAULT_MAX_BYTES_PER_FILE = 1024 * 1024 * 1024

# The default maximum number of bytes to read from a file when using the
# --max-bytes-per-file-with-header option.
DEFAULT_MAX_BYTES_PER_FILE_WITH_HEADER = 1024 * 1024 * 1024

# The default maximum number of bytes to read from a file when using the
# --max-bytes-per-file-without-header option.
DEFAULT_MAX_BYTES_PER_FILE_WITHOUT_HEADER = 1024 * 1024 * 1024

# The default maximum number of bytes to read from a file when using the
# --max-bytes-per-file-with-footer option.
DEFAULT_MAX
