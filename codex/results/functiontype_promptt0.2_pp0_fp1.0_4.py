import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
# Test types.LambdaType
g = lambda: None
assert isinstance(g, types.LambdaType)
# Test types.GeneratorType
def h():
    yield 1

assert isinstance(h(), types.GeneratorType)
# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
# Test types.BuiltinMethodType
assert isinstance(list.append, types.BuiltinMethodType)
# Test types.ModuleType
import sys
assert isinstance(sys, types.ModuleType)
# Test types.MethodType
class A:
    def f(self):
        pass

assert isinstance(A.f, types.MethodType)
# Test types.UnboundMethodType
assert isinstance(A.f, types.UnboundMethodType)
# Test types.TracebackType
try:
    raise Exception
except:
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.Tr
