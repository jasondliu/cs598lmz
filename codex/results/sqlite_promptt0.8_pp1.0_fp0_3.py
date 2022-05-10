import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
try:
    conn = sqlite3.connect(':memory:')
except:
    sys.exit('ERROR: sqlite3 module not found.  Please install the python-sqlite3 package')

# Test libxml2
try:
    libxml2 = ctypes.CDLL(ctypes.util.find_library('xml2'))
except:
    sys.exit('ERROR: libxml2 module not found.  Please install the libxml2-python package')

# Test libght
try:
    libght = ctypes.CDLL(ctypes.util.find_library('ght'))
except:
    sys.exit('ERROR: libght module not found.  Please install the libght package')

## main

if __name__ == "__main__":
    # Run the tests
    import test_http
    test_http.http_test()

    import test_storage
    test_storage.storage_test()

    import test_update
    test_update.update_test()

# vim: set expandtab ts=4 sw=
