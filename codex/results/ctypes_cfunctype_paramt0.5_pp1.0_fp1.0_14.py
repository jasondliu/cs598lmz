import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

class C(object):
    def __init__(self):
        self.lib = ctypes.CDLL('./test.so')
        self.lib.test.argtypes = (ctypes.c_int, ctypes.c_int)
        self.lib.test.restype = ctypes.c_int
        self.lib.test_callback.argtypes = (FUNTYPE, ctypes.c_int, ctypes.c_int)
        self.lib.test_callback.restype = ctypes.c_int

    def test(self, a, b):
        return self.lib.test(a,b)

    def test_callback(self, callback, a, b):
        return self.lib.test_callback(callback, a, b)

def run():
    c = C()
    print c.test(1, 1)
    callback = FUNTYPE(lambda a, b: a + b)
    print c.test_callback(callback, 1,
