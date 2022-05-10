import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

class Foo(object):
    def __init__(self):
        self.lib = ctypes.CDLL('libfoo.so')
        self.lib.foo.argtypes = [ctypes.c_int, ctypes.c_int]
        self.lib.foo.restype = ctypes.c_int

    def foo(self, a, b):
        return self.lib.foo(a, b)

f = Foo()
print f.foo(1, 2)

# Now we want to call the function with a callback
def callback(a, b):
    print a, b
    return a + b

cb = FUNTYPE(callback)

f.lib.bar.argtypes = [ctypes.c_int, FUNTYPE]
f.lib.bar.restype = ctypes.c_int

print f.lib.bar(1, cb)
</code>
The C code for libfoo.so:
<code>int foo(int a,
