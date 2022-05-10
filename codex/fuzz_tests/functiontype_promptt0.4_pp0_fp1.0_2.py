import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)

# Test types.MethodType
class A:
    def m(self): pass
assert isinstance(A.m, types.MethodType)
assert isinstance(A().m, types.MethodType)

# Test types.ModuleType
import sys
assert isinstance(sys, types.ModuleType)

# Test types.LambdaType
l = lambda: 0
assert isinstance(l, types.LambdaType)

# Test types.GeneratorType
def g():
    yield 1
assert isinstance(g(), types.GeneratorType)

# Test types.CodeType
assert isinstance(f.__code__, types.CodeType)

# Test types.TracebackType
try:
    raise Exception
except:
    assert isinstance(sys.exc_info()[2], types.TracebackType)

# Test types.FrameType
assert isinstance(sys._getframe
