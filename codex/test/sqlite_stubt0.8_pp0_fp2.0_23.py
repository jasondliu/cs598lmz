import ctypes
import ctypes.util
import threading
import sqlite3

my_threading_local = threading.local()

class deleting_conn(sqlite3.Connection):
    def __del__(self):
        self.close()

DB_URI = "file:test?mode=memory"

def my_cb(p):
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def test_fn(a, b):
        return a

    a.create_function("test", 2, test_fn)

    my_threading_local.a = a

    return 1

# todo: this seems a bit heavy handed, but i can't figure out a better way to
# force the threading local variable to be set up.
my_cb(None)

l_sqlite3 = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sqlite3'))

l_sqlite3.sqlite3_enable_shared_cache(1)

l_sqlite3.sqlite3_config(5, my_cb)

l_sqlite3.sqlite3_finalize(0)

# this makes sure that our threading local is correctly set up.
my_threading_local.a.close()
my_threading_local.a = None

from .. import util

from .. import extras

from ..results import Results

from ..session import Session
from ..model import *
from ..transaction import Transaction
from ..schema import *
from ..schema_builder import *
from ..schema_builder import _schema_builder_db
from ..adapters import adapter
from ..adapters import adapters

