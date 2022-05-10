import _struct
import threading
import tkinter


import pymysql


def thread_it(func, *args):
    t = threading.Thread(target=func, args=args)
    t.setDaemon(True)
    t.start()


def _async_raise(tid, exctype):
    """raising in threads"""

    if not isinstance(tid, int):
        raise TypeError("id must be integer")
    if not issubclass(exctype, BaseException):
        raise TypeError("exc must be exception type")

    import ctypes
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
        ctypes.c_long(tid), ctypes.py_object(exctype))

    if res == 0:
        raise ValueError("invalid thread ID")
    elif res != 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


