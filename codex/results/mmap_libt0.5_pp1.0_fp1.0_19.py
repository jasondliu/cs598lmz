import mmap
import os
import re
import sys

from . import _compat
from . import _util
from . import _winreg

# The following constants are not defined in Python 3.
if sys.version_info[0] < 3:
    SEEK_SET = 0
    SEEK_CUR = 1
    SEEK_END = 2

# The following constants are not defined in Python 2.
if sys.version_info[0] < 3:
    SEEK_DATA = 3
    SEEK_HOLE = 4

# The following constants are not defined in Python 2.
if sys.version_info[0] < 3:
    O_RDONLY = os.O_RDONLY
    O_WRONLY = os.O_WRONLY
    O_RDWR = os.O_RDWR
    O_APPEND = os.O_APPEND
    O_CREAT = os.O_CREAT
    O_TRUNC = os.O_TRUNC
    O_EXCL = os.O_EXCL
    O_NONBLOCK
