import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
class Bit(object):
    __slots__ = ["_bit", "bits", "_args", "min", "max", "funs"]
    def __init__(self, bits, min=None, max=None, **kw):
        self.bits = bits
        self.min = min
        self.max = max
        self.funs = {}
        self._args = (self,) + (bits,) + (min,) + (max,)
    def set(self, fun, *args):
        a = args if args else self._args
        if not isinstance(fun, FUNTYPE): fun = FUNTYPE(fun)
        self.funs[fun] = a
    def unset(self, fun):
        if fun in self.funs: del self.funs[fun]
    def __call__(self, arg):
        r = arg
        for k in self.funs.iterkeys():
            b, a = self.funs[k], r
            if self.min is not None and b(a) < self.min:
