import ctypes
import ctypes.util
import threading
import sqlite3

from . import common
from .common import *


# Query, multi query, and cut
# ===========================


def query(db, sql, args=[]):
    """Execute SQL query, returning all results.

    `db`:
        DB API 2 connection handle.
    `sql`:
        SQL statement with optional placeholders (`?`).
    `args`:
        One or more argument values to replace placeholders with.

    """
    common.check_type_db(db)
    common.check_type_loop(db.loop)

    select_type = sqlite3.prepare_v2(db.handle, sql, -1, None)
    if select_type == _SQLITE_DONE:
        return None
    elif select_type == _SQLITE_ROW:
        return [row for row in _select_iter(db)]
    elif select_type == _SQLITE_OK:
        return _change_iter(db)
    else:
        sqlite3.finalize(db.handle)
        raise common.Interface
