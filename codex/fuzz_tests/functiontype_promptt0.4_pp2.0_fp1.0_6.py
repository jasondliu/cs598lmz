import types
# Test types.FunctionType
def f(): pass
assert type(f) == types.FunctionType
assert type(f) == types.BuiltinFunctionType

# Test types.LambdaType
l = lambda: None
assert type(l) == types.LambdaType

# Test types.GeneratorType
def g(): yield 1
assert type(g()) == types.GeneratorType

# Test types.CodeType
assert type(f.__code__) == types.CodeType

# Test types.TracebackType
try:
    raise Exception
except:
    tb = sys.exc_info()[2]
    assert type(tb) == types.TracebackType

# Test types.FrameType
def ff(x):
    return sys._getframe()
assert type(ff(1)) == types.FrameType

# Test types.ModuleType
assert type(types) == types.ModuleType

# Test types.BuiltinMethodType
assert type(list.append) == types.BuiltinMethodType

# Test types.MethodType
class C(object):
    def m(
