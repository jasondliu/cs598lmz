import types
# Test types.FunctionType (issue 839287)
class A:
    def f(self): pass
try:
    types.FunctionType(A.f, globals())
except TypeError:
    pass
else:
    print("Should have raised TypeError")

class B:
    pass
B.m = lambda self: 42
try:
    types.FunctionType(B.m, globals())
except TypeError:
    pass
else:
    print("Should have raised TypeError")
