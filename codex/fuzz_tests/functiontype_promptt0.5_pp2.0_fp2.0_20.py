import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
# Test types.BuiltinFunctionType
def g():
    pass
assert isinstance(g, types.BuiltinFunctionType)
# Test types.GeneratorType
def h():
    yield 1
assert isinstance(h(), types.GeneratorType)
# Test types.GeneratorType
def i():
    yield 1
assert isinstance(i(), types.GeneratorType)
# Test types.LambdaType
l = lambda x: x
assert isinstance(l, types.LambdaType)
# Test types.MethodType
class A(object):
    def f(self):
        pass
assert isinstance(A.f, types.MethodType)
# Test types.ModuleType
import sys
assert isinstance(sys, types.ModuleType)
# Test types.UnboundMethodType
class B(object):
    def f(self):
        pass
assert isinstance(B.f, types.UnboundMethodType)
# Test types.TypeType
assert isinstance(int, types.TypeType
