import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

class Foo(object):
    def __init__(self):
        self.callback = FUNTYPE(self.callback)

    def register(self, f):
        f.argtypes = (FUNTYPE,)
        f.restype = None
        f(self.callback)

    def callback(self, n):
        print "Callback called with %d" % n
        return 0

f = ctypes.CDLL('./libfoo.so')
foo = Foo()
foo.register(f.register_callback)
</code>

