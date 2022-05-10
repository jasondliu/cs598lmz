import ctypes
# Test ctypes.CFUNCTYPE
class Block(object):
    def __init__(self, argtypes, restype, func):
        self.argtypes = argtypes
        self.restype = restype
        self.func = func
        self.function = CFUNCTYPE(restype, *argtypes)(func)

def my_callback(i, s):
    return i + len(s)

block = Block((c_int, c_char_p), c_int, my_callback)
print(block.function(5, b"Hello"))

# Test ctypes.WINFUNCTYPE
class Window(object):
    def __init__(self, func = None):
        self.func = func
        self.window = WINFUNCTYPE(c_int, HWND, c_uint, WPARAM, LPARAM)(func)

def my_func(hwnd, msg, wp, lp):
    # ...
    return 0

wnd = Window(my_func)
#...
DispatchMessage(byref(msg))

# Test ctypes.PY
