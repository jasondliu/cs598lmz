import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

class Database(object):
    def __init__(self, db_file):
        self.lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3"))
        self.db_file = db_file
        self.lib.sqlite3_open(db_file, ctypes.byref(self.db_ptr))
        self.lib.sqlite3_exec(self.db_ptr, "PRAGMA journal_mode=WAL", None, None, None)

    def finalize(self):
        self.lib.sqlite3_close(self.db_ptr)

    def execute(self, sql, params=()):
        self.lib.sqlite3_prepare_v2(self.db_ptr, sql, -1, ctypes.byref(self.stmt_ptr), None)
        for idx, param in enumerate(params):
            param_ty, param_val = param
            if param_ty == "INTEGER":
                param_ty = self.lib.SQL
