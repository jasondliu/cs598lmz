import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() with a URI
#
# The tests in this file cover the following URI parameters:
#
# - cache
# - mode
# - vfs
#
# The following are implicitly tested:
#
# - database name
# - hostname
# - query parameters
#
# The following are not tested:
#
# - auth_user
# - auth_password
# - user_name
# - password
# - port
# - fragment
# - protocol
# - path
# - params
#
# The following are not implemented:
#
# - auth_user
# - auth_password
# - query parameters
#
# See also: http://www.sqlite.org/uri.html

# This global variable is used by the threading test to communicate with the
# main thread.
result = None

# This is the custom VFS used by the tests.
vfs_name = 'test-vfs'

# This is the custom VFS used by the tests.
vfs_name2 = 'test-vfs-2'

# This is the custom VFS used by
