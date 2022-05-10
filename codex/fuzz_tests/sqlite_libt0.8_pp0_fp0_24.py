import ctypes
import ctypes.util
import threading
import sqlite3
import weakref

__all__ = ["init", "create_isolation_layer", "finalize",
           "DatabaseError", "get_total_changes", "enable_shared_cache",
           "register_adapter", "register_converter", "adapt", "convert_date",
           "convert_timestamp", "complete_statement", "complete_delete_statement",
           "complete_insert_statement", "complete_update_statement", "complete_select_statement",
           "complete_rollback_savepoint_statement", "complete_release_savepoint_statement",
           "complete_begin_transaction_statement", "complete_commit_statement"]

try:
    from . import _sqlite3 as sqlite3
except ImportError:
    pass

if sqlite3.sqlite_version_number >= 3007010:
    _threadsafety = 1
    _have_isolation_layer = True
else:
    if sqlite3.sqlite_version_number > 3007007:
        _threadsafety = 2
    else:
        _threadsafety = 0
