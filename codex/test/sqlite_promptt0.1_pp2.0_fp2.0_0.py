import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared')

# This is a test of the sqlite3 module.  It is not a complete test.
# It does not test the ability to compile the module.  It does not
# test the threading or thread safety of the module.  It does not
# test the ability to use the module to access databases on disk.
# It does not test the full feature set of the module.

# The tests are run twice.  The first time, the module is imported
# normally.  The second time, the module is imported using the
# -P option to disable the Python-level statement cache.

# The tests are run in a sub-interpreter to ensure that the module
# is re-initialized properly.

# The tests are run in a sub-thread to ensure that the module is
# thread-safe.

# The tests are run with a memory database and a disk database to
# ensure that the module can handle both.

# The tests are run with a shared cache and a private cache to
# ensure that the module can handle both.

# The tests are run with a UTF
