import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")
import _sqlite3

# TODO:
# - implement a way to set the timeout for blocking operations
# - implement a way to set the default encoding for text
# - implement a way to set the default error handler
# - implement a way to set the default text factory
# - implement a way to set the default isolation_level
# - implement a way to set the default factory
# - implement a way to set the default row factory
# - implement a way to set the default cursor factory

# XXX: we don't support the following functions:
# - sqlite3_backup_init
# - sqlite3_backup_finish
# - sqlite3_backup_step
# - sqlite3_blob_open
# - sqlite3_blob_bytes
# - sqlite3_blob_read
# - sqlite3_blob_write
# - sqlite3_blob_reopen
# - sqlite3_blob_close
# - sqlite3_vfs_find
# - sqlite3_vfs_register
# - sql
