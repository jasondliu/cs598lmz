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

