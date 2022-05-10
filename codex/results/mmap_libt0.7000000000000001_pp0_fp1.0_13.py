import mmap
import os
from ctypes import *
from ctypes.util import find_library
import struct
from struct import pack, unpack

from . import structures
from . import exceptions
from . import util


#
# As a sidenote: apparently fopen from glibc does a very optimized job
# of parsing the file modes and flags. glibc will optimise for most
# common cases and has a very nice fallback and error checking when
# there are problems.
#

#
# These are the default flags for a file.
#
O_RDONLY = 0x0000
O_WRONLY = 0x0001
O_RDWR = 0x0002
O_CREAT = 0x0040
O_TRUNC = 0x0200
O_APPEND = 0x0400
O_EXCL = 0x0800
O_NOCTTY = 0x20000
O_NONBLOCK = 0x800

#
# These are the default file permissions.
#
S_IRWXU = 0o700
S_IRUSR = 0o400
S_
