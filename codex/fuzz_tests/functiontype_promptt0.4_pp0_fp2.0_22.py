import types
# Test types.FunctionType
def f(): pass
print type(f) == types.FunctionType

# Test types.LambdaType
g = lambda: None
print type(g) == types.LambdaType

# Test types.GeneratorType
def gen():
    yield 1
    yield 2
    yield 3
print type(gen()) == types.GeneratorType

# Test types.BuiltinFunctionType
print type(len) == types.BuiltinFunctionType

# Test types.BuiltinMethodType
print type([].append) == types.BuiltinMethodType

# Test types.MethodType
class Foo(object):
    def bar(self):
        pass
foo = Foo()
print type(foo.bar) == types.MethodType

# Test types.UnboundMethodType
print type(Foo.bar) == types.UnboundMethodType

# Test types.ModuleType
import sys
print type(sys) == types.ModuleType

# Test types.TracebackType
try:
    1/0
except:
    tb = sys.exc_info()[2]

