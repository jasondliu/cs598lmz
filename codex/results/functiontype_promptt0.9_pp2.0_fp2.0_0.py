import types
# Test types.FunctionType in different ways.
# Also test this with callables that were not defined with def, lambda or def f(): return lambda: ...
# Also test the doc attribute.
# Also test the attributes defined by the 'function' metaclass (__globals__, __closure__, etc.)
# Also test the argument to __code__ (docstring, keyword-only arguments, etc.)

#NOTE: these tests are not exhaustive

class A:
    # Testing object methods...
    def m1(self): pass
    m2 = lambda self: None
    def m3(self):
        return lambda self=self: None
    def m4(self, x, y=1, *, z="x", **kwargs): pass
    # Testing class methods...
    def m5(cls, x, y=1, *, z="x", **kwargs): pass
    m6 = classmethod(lambda cls: None)
    @classmethod
    def m7(cls): pass
    @classmethod
    def m8(cls, x, y=1, *, z="y",
