import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:test?mode=memory&cache=shared', uri=True)

import_name = ctypes.util.find_library('lz4')
if import_name is None:
    raise ImportError('Could not find lz4 library')
lz4 = ctypes.CDLL(import_name)

# Python 3.3+ has buffer protocol
# See http://www.python.org/dev/peps/pep-3118/

# Python 3.3+ has ctypes.memoryview
# See http://www.python.org/dev/peps/pep-3118/

# Python 3.2+ has ctypes.c_ssize_t
# See http://www.python.org/dev/peps/pep-3118/

# Python 3.0+ has ctypes.c_int
# See http://www.python.org/dev/peps/pep-3118/

# Python 2.6+ has ctypes.c_size_t
# See http://www.python.org/dev/peps/pep
