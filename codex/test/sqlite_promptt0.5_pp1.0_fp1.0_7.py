import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file::memory:?cache=shared', uri=True)
# Test sqlite3.connect('file::memory:?cache=private', uri=True)

# The following lines are to make sure that modules are reloaded when
# they have changed.
import imp
import sys
imp.reload(sys.modules['sqlite3'])

# The following lines are to make sure that the tests are run with the
# same version of the sqlite3 library as the interpreter.
import sys
if sys.version_info.major < 3:
    import sqlite3 as _sqlite3
else:
    import _sqlite3 as _sqlite3

sqlite3 = _sqlite3

# The following lines are to make sure that the tests are run with the
# same version of ctypes as the interpreter.
import ctypes
if sys.version_info.major < 3:
    import ctypes as _ctypes
else:
    import _ctypes as _ctypes

ctypes = _ctypes

