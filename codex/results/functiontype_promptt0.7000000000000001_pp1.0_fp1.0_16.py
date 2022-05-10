import types
# Test types.FunctionType
def f():
    pass
def g():
    return 42

assert isinstance(f, types.FunctionType)
assert isinstance(g, types.FunctionType)
# Test types.MethodType
class C:
    def meth(self):
        pass

assert isinstance(C().meth, types.MethodType)
# Test types.LambdaType
assert isinstance(lambda : 42, types.LambdaType)
assert isinstance(lambda x,y: x+y, types.LambdaType)
assert isinstance(lambda self: None, types.LambdaType)
# Test types.GeneratorType
def gen():
    yield 42

g = gen()

assert isinstance(g, types.GeneratorType)
# Test types.BuiltinFunctionType
assert isinstance(hex, types.BuiltinFunctionType)
# Test types.BuiltinMethodType
assert isinstance('foo'.upper, types.BuiltinMethodType)
# Test types.ModuleType
try:
    import posix
except ImportError:
    print "SKIP"
    import sys
