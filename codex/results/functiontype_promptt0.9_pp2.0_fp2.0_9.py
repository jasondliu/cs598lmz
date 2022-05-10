import types
# Test types.FunctionTypes and types.MethodType (in the form of object.methodobj).
def checkfun(fn, fv, mv, mvs):
    print fn.__name__, "function", hex(id(fn))
    if fn.__name__ == 'function':
        assert fv[0] is fn
    elif fn.__name__ == 'boundmethod':
        assert mv[0] is fn
    else:
        assert mv[0] is fn, fn.__name__
    for mv in mvs:
        print "    method", hex(id(mv)), mv.__name__
        assert type(mv) is types.MethodType
        assert mv.__self__ is fn # or could be any one of the other possible objects returned by __get__()

class C(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def method(self):
        return self.a + self.b
    def methodb(self):
        return self.b + self.a

