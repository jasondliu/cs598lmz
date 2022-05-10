import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
# Test types.LambdaType
g = lambda x: x

assert isinstance(g, types.LambdaType)
# Test types.GeneratorType
def h():
    yield 1

assert isinstance(h(), types.GeneratorType)
# Test types.MethodType
class A:
    def m(self):
        pass

assert isinstance(A.m, types.MethodType)
# Test types.UnboundMethodType
class B:
    def m():
        pass

assert isinstance(B.m, types.UnboundMethodType)
# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
# Test types.BuiltinMethodType
assert isinstance(list.append, types.BuiltinMethodType)
# Test types.ModuleType
assert isinstance(types, types.ModuleType)
# Test types.TracebackType
try:
    raise Exception
except:
    import sys
    assert isinstance(sys.exc_
