import types
# Test types.FunctionType
def func(x):
    return x

assert isinstance(func, types.FunctionType)
# Test types.LambdaType
lamb = lambda x: x

assert isinstance(lamb, types.LambdaType)
# Test types.GeneratorType
def gen(x):
    for i in range(x):
        yield i

assert isinstance(gen(5), types.GeneratorType)
# Test types.BuiltinFunctionType
assert isinstance(print, types.BuiltinFunctionType)
# Test types.BuiltinMethodType
assert isinstance(print.__call__, types.BuiltinMethodType)
# Test types.MethodType
class A:
    def __init__(self):
        self.x = 5
    def method(self):
        return self.x

assert isinstance(A.method, types.MethodType)
# Test types.UnboundMethodType
assert isinstance(A.method.__get__(A()), types.UnboundMethodType)
# Test types.ModuleType
import sys
assert isinstance(sys, types.
