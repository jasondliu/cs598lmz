import types
# Test types.FunctionType
def f(): pass
assert type(f) == types.FunctionType

# Test types.BuiltinFunctionType
assert type(abs) == types.BuiltinFunctionType

# Test types.MethodType
class C:
    def m(self): pass
assert type(C.m) == types.MethodType

# Test types.ModuleType
assert type(types) == types.ModuleType

# Test types.TracebackType
try:
    raise Exception
except:
    tb = sys.exc_info()[2]
assert type(tb) == types.TracebackType

# Test types.FrameType
def f():
    return sys._getframe()
assert type(f()) == types.FrameType

# Test types.CodeType
assert type(f.__code__) == types.CodeType

# Test types.GeneratorType
def f():
    yield 1
assert type(f()) == types.GeneratorType

# Test types.GetSetDescriptorType
class C:
    def __get__(self, obj, t): pass
assert type
