import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared', uri=True)

#
# Global variables
#

# If we're running on Mac OS X, load the Security framework.  This is needed to
# enable the SecureTransport interface.
if sys.platform == 'darwin':
    ctypes.cdll.LoadLibrary(ctypes.util.find_library('Security'))

#
# Shared memory support
#

# sqlite3.connect() with uri=True requires file system access, which is not
# available on Android.  In this case, we fall back to using a shared memory
# buffer.
_use_file_cache = sqlite3.sqlite_version_info >= (3, 7, 7)

if not _use_file_cache:
    _cache_lock = threading.Lock()
    _cache_buffer = None

#
# Public functions
#

def connect(database, timeout=5.0, isolation_level=None, detect_types=0,
            check_same_thread=False, factory=None, cached_statements=100):
