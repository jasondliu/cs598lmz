import types
# Test types.FunctionType
def foo():
    pass

assert type(foo) is types.FunctionType
assert type(foo) is types.BuiltinFunctionType
assert type(foo) is types.BuiltinMethodType

# Test types.LambdaType
bar = lambda: None
assert type(bar) is types.LambdaType

# Test types.MethodType
class Foo(object):
    def bar(self):
        pass

assert type(Foo.bar) is types.MethodType
assert type(Foo().bar) is types.MethodType

# Test types.UnboundMethodType
assert type(Foo.bar) is types.UnboundMethodType

# Test types.BuiltinMethodType
assert type(Foo.__new__) is types.BuiltinMethodType

# Test types.ModuleType
import sys
assert type(sys) is types.ModuleType

# Test types.TypeType
assert type(Foo) is types.TypeType

# Test types.TracebackType
try:
    raise Exception()
except:
    tb = sys.exc_info()
