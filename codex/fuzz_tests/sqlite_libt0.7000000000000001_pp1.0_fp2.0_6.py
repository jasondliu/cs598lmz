import ctypes
import ctypes.util
import threading
import sqlite3
import os
import re
import sys
import logging

import pbclient
import pbutil

# The default log level is set to ERROR so that we don't spam stdout.
# The user can override this in settings.py if they want to see more info.
LOG_LEVEL = logging.ERROR

# The default name of the library to load.
LIBRARY_NAME = "libcubeb.so.0"

def load_libcubeb():
    """Load the libcubeb library.

    This function will try to load libcubeb from a few different locations,
    and will raise an ImportError if it can't find the library.
    """
    # Try to load the library directly.
    try:
        libcubeb = ctypes.CDLL(LIBRARY_NAME)
        return libcubeb
    except OSError:
        pass

    # Try to load the library using ctypes.util.find_library.
    # This is a ctypes utility function that will try to find the given
    # library on the system using the ctypes
