import ctypes.util
import threading
import sqlite3
class deleting_conn(sqlite3.Connection):
    def __del__(self):
        self.close()
ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(threading.get_ident()),
                                           ctypes.py_object(KeyboardInterrupt))
