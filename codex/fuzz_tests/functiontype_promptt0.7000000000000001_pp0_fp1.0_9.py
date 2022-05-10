import types
# Test types.FunctionType, types.MethodType, types.BuiltinMethodType, types.BuiltinFunctionType

# Test FunctionType
def f(*args): pass
def f2(*args, **kwds): pass
def f3(*args, a=3, **kwds): pass
def f4(a=3, b=4, *args, **kwds): pass
def f5(*args, a=3, b=4, **kwds): pass
f.attr = 3

assert isinstance(f, types.FunctionType)
assert isinstance(f2, types.FunctionType)
assert isinstance(f3, types.FunctionType)
assert isinstance(f4, types.FunctionType)
assert isinstance(f5, types.FunctionType)

# Test MethodType
class C:
    def f(*args, **kwds): pass
    def f2(*args, a=3, **kwds): pass
    def f3(a=3, b=4, *args, **kwds): pass
    def f4(*args, a=3, b=4, **kwds): pass

