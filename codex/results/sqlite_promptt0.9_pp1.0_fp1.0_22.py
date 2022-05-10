import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()


class Error(Exception):
    pass

def _path(*args):
    '''Joins "args" into a file path.
    The nodes in "args" must be joined by forward slashes, as in a URL.'''
    return '/'.join(args)


# The number of seconds an idle thread lives before it is terminated.
TIMEOUT = 60
# The interval in seconds between checks for idle threads.
CHECK_INTERVAL = 10
# Exposed to the JavaScript API.
NEWPAGE_FLAG = -1

# Indicates that the first use of a key will be insertion (into an array).
INSERT_FLAG = -1

# Controls the output of the JavaScript API.  True enables debugging output.
DEBUG_FLAG = False

# The minimum value for a differentiator.
DEF_ID_MIN = 1
# The maximum value for a differentiator.
DEF_ID_MAX = 1000
# The length of the differentiator as a string.
STRING_LENGTH = int(math.log10(DEF_ID_MAX) + 2)

# The array used for "def_
