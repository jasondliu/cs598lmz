import ctypes
import ctypes.util
import threading
import sqlite3

# This is some sort of build info.
# Check include/libfds/api.h for details
# We need these constants to check compatibility
# of loaded library and our application
FDS_API_VERSION = 1
FDS_API_BUILD = 4
FDS_API_MINOR = 1
# Set export version
FDS_API_EXPORT_VERSION = 1

# Note: The library can be loaded only once in a single application
# (e.g. in one Python process)

# Flag if the library has been already loaded (and can be used)
_is_api_loaded = False

# Python CFFI library
_api = None

# Load default paths
_ld_paths = ["/usr/local/lib/libfds.so", "/usr/lib/libfds.so"]


def update_ld_paths(paths):
    """
    Update paths to libfds library
    :param paths: List of paths to check
    """
    global _ld_paths
    _ld_paths = paths


def update_struct
