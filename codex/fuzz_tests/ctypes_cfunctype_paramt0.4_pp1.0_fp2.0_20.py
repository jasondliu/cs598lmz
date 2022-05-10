import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(arg):
    print('callback called with arg', arg)
    return 0

CMPFUNC = FUNTYPE(callback)

class Foo(ctypes.Structure):
    _fields_ = [('bar', ctypes.c_int),
                ('func', CMPFUNC)]

foo = Foo()
foo.bar = 42
foo.func(foo.bar)
</code>
This prints
<code>callback called with arg 42
</code>

