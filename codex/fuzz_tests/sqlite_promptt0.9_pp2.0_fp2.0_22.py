import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file::memory:?cache=shared')
import _ctypes
import array
# stdlock is at least 20 bytes (64 bit)
assert array.array("P", [ctypes.pythonapi.PyThread_get_thread_ident()]).itemsize >= 20

libc = ctypes.CDLL("libc.so.6")

# Test our _ctypes._CFuncPtr and pure python alternative
class CustomFunctionPointer:
    tp_name = "CustomFunctionPtr"
    _restype_ = ctypes.c_int
    _flags_ = (("stdcall",)
               if sys.platform == "win32" else ())
    _argtypes_ = ()

    def __init__(self, closure):
        self._closure = closure

    def get(self):
        return self._closure

    def __call__(self, *args, **kwargs):
        return self.get()(*args, **kwargs)

class CustomFunc:
    def __call__(self, *args, **kwargs):
        return 0


print("calling a custom function
