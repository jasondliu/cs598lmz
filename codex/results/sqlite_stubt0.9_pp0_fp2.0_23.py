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

FTS3_TOKENIZER_SUFFIX = '-fts3tokenizer'
FTS3_TOKENIZER_FACTORY = FTS3_TOKENIZER_SUFFIX + 'sqlite3_tokenizer_module_export'

class Tokenizer():
    def __init__(self, dll_path):
        self.dll = ctypes.CDLL(dll_path)
        self.dll.sqlite3_tokenizer_module_export.restype = ctypes.POINTER(
                        sqlite3.sqlite3_tokenizer_module)
        self.dll.sqlite3_tokenizer_module_export.argtypes = [
                        ctypes.c_char_p,
                        ctypes.c_void_p,
                        ctypes.c_void_p]
        self.dll.pysqlite3_tokenizer_export.restype = ctypes.POINTER(
                        sqlite3.sqlite3_tokenizer_module)
        self.dll.pysqlite3_tokenizer_export.argtypes = [

