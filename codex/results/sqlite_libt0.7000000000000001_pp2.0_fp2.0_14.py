import ctypes
import ctypes.util
import threading
import sqlite3
from collections import namedtuple

import sqlitefts

libc = ctypes.CDLL(ctypes.util.find_library('c'), use_errno=True)

def _check_sqlite(result, func, arguments):
    if isinstance(result, str):
        return result
    elif result != sqlite3.OK:
        raise Exception('{} failed with {}'.format(func, arguments))
    return None

sqlite3.register_adapter(dict, sqlite3.prepare.Binary)
sqlite3.register_converter('fts4dict', sqlitefts.as_dict)

sqlite3.register_adapter(list, sqlite3.prepare.Binary)
sqlite3.register_converter('ftslist', lambda s: s.split(b'\x1f'))

class Database(sqlite3.Connection):
    def __init__(self, filename, **kwargs):
        super().__init__(filename, detect_types=sqlite3.PARSE_DECLTYPES,
