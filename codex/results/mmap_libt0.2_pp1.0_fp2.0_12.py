import mmap
import os
import sys
import time

from . import common
from . import config
from . import constants
from . import exceptions
from . import log
from . import util
from . import vfs

# pylint: disable=too-many-lines

#
# Constants
#

# The maximum number of times to retry a failed read.
_READ_RETRIES = 5

# The maximum number of times to retry a failed write.
_WRITE_RETRIES = 5

# The maximum number of times to retry a failed seek.
_SEEK_RETRIES = 5

# The maximum number of times to retry a failed truncate.
_TRUNCATE_RETRIES = 5

# The maximum number of times to retry a failed fsync.
_FSYNC_RETRIES = 5

# The maximum number of times to retry a failed fstat.
_FSTAT_RETRIES = 5

# The maximum number of times to retry a failed ftruncate.
_FTRUNCATE_RETRIES = 5
