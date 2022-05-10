import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
# Test types.LambdaType
assert isinstance(lambda: None, types.LambdaType)
# Test types.GeneratorType
def g():
    yield 1
assert isinstance(g(), types.GeneratorType)
# Test types.MethodType
class A:
    def m(self):
        pass

assert isinstance(A().m, types.MethodType)
# Test types.BuiltinFunctionType
import math
assert isinstance(math.sin, types.BuiltinFunctionType)
# Test types.BuiltinMethodType
assert isinstance(math.sqrt.__doc__, types.BuiltinMethodType)
# Test types.ModuleType
import sys
assert isinstance(sys, types.ModuleType)
# Test types.TracebackType
try:
    1/0
except:
    import sys
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.TracebackType)
    assert isinstance(tb.tb_
