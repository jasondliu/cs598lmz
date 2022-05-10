import weakref

from . import get_debug_flag
from . import logger, log_level

if get_debug_flag():
    # this is a trick to make the "assert" statement
    # to be compiled even in release mode.
    def __assert(cond):
        if not cond:
            raise Exception("Assertion Failed")
    assert = __assert

# Importing 'os' may fail when the tarball is unpacked into
# a directory that is already present, so we do it in a
# try/except clause and print a warning to stderr if it fails.
try:
    import os
except ImportError:
    logger.critical("Could not import os module. This is needed for "
                    "file I/O and other basic operations. Please "
                    "install it and try again.")
    raise

try:
    import sys
except ImportError:
    logger.critical("Could not import sys module. This is needed for "
                    "file I/O and other basic operations. Please "
                    "install it and try again.")
    raise

try:
    import time
except
