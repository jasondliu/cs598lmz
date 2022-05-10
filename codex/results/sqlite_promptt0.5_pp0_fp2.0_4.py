import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connection.total_changes

# This is a manual test, not an automatic one.

# This test is expected to pass, but it is not expected to
# pass on all platforms.

# This test uses ctypes to access the internal sqlite3_memory_used()
# interface.  The internal sqlite3_memory_used() interface is not
# part of the public API and hence is not supported.

# This test is not expected to work on Windows.

# This test is not expected to work on MacOS.

# This test is not expected to work on the 64-bit build.

# This test is not expected to work on the mingw build.

# This test is not expected to work on the TCC build.

# This test is not expected to work on the pysqlite build.

# This test is not expected to work on the sqlite amalgamation build.

# This test is not expected to work on the sqlite amalgamation
# build with TCC.

# This test is not expected to work on the sqlite amalgamation
# build with pysqlite.

#
