import ctypes
import ctypes.util
import threading
import sqlite3
import os.path
import subprocess
import socket
import atexit
import sys
import psutil

import lnk

# Set up basic ctypes structures and constants.

# For the x86, x86_64, and arm architectures, the pefile library
# uses the same structures as the win32 API.

import pefile

try:
    from pefile import IMAGE_OPTIONAL_HEADER
except ImportError:
    # When running on an ARM device, the pefile library does not
    # have an IMAGE_OPTIONAL_HEADER structure defined.
    #
    # The IMAGE_OPTIONAL_HEADER structure is not needed for
    # the ARM architecture, so this is safe to ignore.

    pass

import pefile.peutils

# The required libraries are not available on the ARM architecture.
#
# The missing libraries are not needed for the ARM architecture,
# so this is safe to ignore.

