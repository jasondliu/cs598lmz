import mmap
import os
import re
import sys
import time

from . import _util
from . import _winreg

if sys.platform == 'win32':
    import win32api
    import win32con
    import win32event
    import win32file
    import win32pipe
    import win32process
    import win32security
    import win32ts


#
# Constants
#

# The maximum number of bytes to read from a pipe at a time.
PIPE_BUFFER_SIZE = 4096

# The maximum number of bytes to read from a socket at a time.
SOCKET_BUFFER_SIZE = 4096

# The maximum number of bytes to read from a file at a time.
FILE_BUFFER_SIZE = 4096

# The maximum number of bytes to read from a file at a time.
FILE_BUFFER_SIZE = 4096

# The maximum number of bytes to read from a file at a time.
FILE_BUFFER_SIZE = 4096

# The maximum number of bytes to read from a file at a time.
FILE_BUFFER_SIZE = 4096

