import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_void_p,ctypes.c_void_p)

class Delegate(object):
    def __init__(self, function):
        self._function = function
        self._f = FUNTYPE(function)

    def Call(self, *args):
        self._function(self, *args)

def f(delegate, *args):
    print "f", delegate, args

d = Delegate(f)
d.Call(1,2,3)
</code>

