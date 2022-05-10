import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)

# Test types.GeneratorType
g = (i for i in range(10))
assert isinstance(g, types.GeneratorType)

# Test types.BuiltinFunctionType
class A:
    def f(): pass
assert isinstance(f, types.BuiltinFunctionType)
assert isinstance(A.f, types.BuiltinFunctionType)

# Test built-in function types
assert isinstance(print, types.BuiltinFunctionType)
assert isinstance(len, types.BuiltinFunctionType)

# Test types.MethodType
class B:
    def f(self): pass
assert isinstance(B().f, types.MethodType)

# Test types.ModuleType
import os
assert isinstance(os, types.ModuleType)

# Test types.TracebackType
try:
    1/0
except:
    import sys
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.TracebackType)

# Test types
