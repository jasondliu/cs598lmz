import ctypes
# Test ctypes.CFUNCTYPE
class Foo(object):
    def __init__(self): pass
class Bar(object):
    def __init__(self): pass
CALLBACKFUNC = ctypes.CFUNCTYPE(None)
data = []
def callbackfunc():
    data.append(1)
c = CALLBACKFUNC(callbackfunc)
import sys
if sys.platform == "win32":
    CALLBACKFUNC = ctypes.WINFUNCTYPE(None)
    data = []
    def callbackfunc():
        data.append(1)
    c = CALLBACKFUNC(callbackfunc)
    lib = ctypes.CDLL("kernel32.dll")
    MessageBox = lib.MessageBoxA
    MessageBox.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
    MessageBox.restype = ctypes.c_int
    MessageBox(0, b"hello world", b"hello world", 0)
