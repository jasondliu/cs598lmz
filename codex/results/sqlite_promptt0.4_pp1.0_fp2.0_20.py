import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

# The following is a hack to make sure we are using the correct library.
# This is only needed for Mac OS X, and only for the system Python.
# For MacPorts or Homebrew, or any other Python, this is not needed.
#
# The problem is that Mac OS X includes an sqlite3 library with the OS,
# but this is the wrong version (it's too old).  The right version is
# in /opt/local/lib, but we need to make sure that ctypes finds it
# there.  The ctypes.util.find_library() function searches a bunch of
# locations, but it doesn't look in /opt/local/lib.  So, we monkey-patch
# that function to look in the right place.

if sys.platform == 'darwin':
    import os
    import ctypes.util
    def mac_find_library(name):
        if name == 'sqlite3':
            return '/opt/local/lib/libsqlite3.dylib'
        return None
    ctypes.util.find_library = mac_find
