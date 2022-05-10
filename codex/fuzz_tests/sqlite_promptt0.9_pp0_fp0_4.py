import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connected() because it will not work with a string.
assert isinstance(sqlite3.connect(':memory:').__enter__(), sqlite3.Connection)

import larch
from larch import Interpreter, use_plugin_path, group
from larch.utils.sqlite_utils import _sqlite_wrap, _sqlite_get_columns
from larch.utils.sqlite_utils import _sqlite_get_tables, _sqlite_num_tables

def test_wrap_callback():
    'Test _sqlite_wrap to see if it works.'

    db_file = 'test.db'
    @_sqlite_wrap
    def _no_dbname_callback(f, data):
        'Callback without a DB name argument.'
        f(data, 'This is data!')

    @_sqlite_wrap
    def _dbname_callback(f, data):
        'Callback with a DB name argument.'
        f(data, 'test.db', 'Data goes here')

    @_sqlite_wrap
    def _no_dbname_
