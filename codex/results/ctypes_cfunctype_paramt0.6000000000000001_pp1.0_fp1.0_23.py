import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)

class Foo(object):
    def __init__(self):
        self.f = FUNTYPE(self.bar)
    def bar(self, arg):
        print arg
        return 42

f = Foo()
f.f("hello")
</code>

