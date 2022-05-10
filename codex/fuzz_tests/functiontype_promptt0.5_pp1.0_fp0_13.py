import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
# Test types.LambdaType
g = lambda: None
assert isinstance(g, types.LambdaType)
# Test types.GeneratorType
def gen(): yield
assert isinstance(gen(), types.GeneratorType)
# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
# Test types.BuiltinMethodType
assert isinstance(dict.fromkeys, types.BuiltinMethodType)
# Test types.MethodType
class D:
    def foo(self): pass
d = D()
assert isinstance(d.foo, types.MethodType)
# Test types.UnboundMethodType
assert isinstance(D.foo, types.UnboundMethodType)
# Test types.ModuleType
import sys
assert isinstance(sys, types.ModuleType)
# Test types.TracebackType
try: 1/0
except: tb = sys.exc_info()[2]
assert isinstance(tb, types.TracebackType)
# Test types
