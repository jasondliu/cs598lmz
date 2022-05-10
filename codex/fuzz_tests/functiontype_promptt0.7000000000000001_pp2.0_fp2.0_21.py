import types
# Test types.FunctionType()
assert isinstance(lambda: None, types.FunctionType)
assert not isinstance(lambda: None, types.LambdaType)

def f(): pass

assert isinstance(f, types.FunctionType)
assert not isinstance(f, types.LambdaType)
# Test types.BuiltinFunctionType()
assert not isinstance(lambda: None, types.BuiltinFunctionType)
assert not isinstance(lambda: None, types.BuiltinMethodType)

# Test types.MethodType()
a = (1, 2)
assert not isinstance(a.count, types.MethodType)
assert not isinstance(a.count, types.BuiltinMethodType)

class A:
    def m(self): pass

a = A()
assert isinstance(a.m, types.MethodType)
assert not isinstance(a.m, types.BuiltinMethodType)

# Test types.ModuleType()
import sys
assert isinstance(sys, types.ModuleType)

# Test types.TracebackType()
try:
    raise Exception("test")

