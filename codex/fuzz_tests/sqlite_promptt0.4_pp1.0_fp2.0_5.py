import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

# NOTE: This is a temporary hack to allow the use of the sqlite3 module
# without it being installed on the system.
#
# This is necessary because the sqlite3 module is not packaged with the
# Python standard library.
#
# This hack is based on the following StackOverflow answer:
# http://stackoverflow.com/a/8356888/145400

# We use ctypes to load the sqlite3 module from the local directory.
# This is necessary because the sqlite3 module is not packaged with the
# Python standard library.

# This is a list of all the required symbols.
sqlite3_symbols = [
    'sqlite3_aggregate_context',
    'sqlite3_aggregate_count',
    'sqlite3_auto_extension',
    'sqlite3_backup_finish',
    'sqlite3_backup_init',
    'sqlite3_backup_pagecount',
    'sqlite3_backup_remaining',
    'sqlite3_backup
