import types
# Test types.FunctionType
def f(x):
    return x
assert type(f) is types.FunctionType
# Test types.LambdaType
g = lambda x: x
assert type(g) is types.LambdaType
# Test types.GeneratorType
def h():
    yield 1
assert type(h()) is types.GeneratorType
# Test types.MethodType
class A:
    def f(self):
        pass
assert type(A.f) is types.MethodType
# Test types.ModuleType
import sys
assert type(sys) is types.ModuleType
# Test types.BuiltinFunctionType
assert type(abs) is types.BuiltinFunctionType
# Test types.BuiltinMethodType
assert type(dict.fromkeys) is types.BuiltinMethodType
# Test types.TypeType
assert type(int) is types.TypeType
# Test types.UnboundMethodType
assert type(A.f) is types.UnboundMethodType
# Test types.TracebackType
try:
    1/0
except ZeroDivisionError:
    assert type(sys.exc_
