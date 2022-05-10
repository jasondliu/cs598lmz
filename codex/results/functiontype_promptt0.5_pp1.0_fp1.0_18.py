import types
# Test types.FunctionType
def f(x):
    return x + 1

assert isinstance(f, types.FunctionType)
assert isinstance(lambda x: x, types.FunctionType)
# Test types.LambdaType
assert isinstance(lambda x: x, types.LambdaType)
assert not isinstance(f, types.LambdaType)
# Test types.GeneratorType
def gen():
    yield 1

assert isinstance(gen(), types.GeneratorType)
# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
# Test types.BuiltinMethodType
assert isinstance([].append, types.BuiltinMethodType)
# Test types.ModuleType
import sys
assert isinstance(sys, types.ModuleType)
# Test types.MethodType
def f(x):
    return x + 1

assert isinstance(f, types.FunctionType)
assert isinstance(f, types.MethodType)
assert isinstance(f(1), types.MethodType)
# Test types.UnboundMethodType
class C(object):
   
