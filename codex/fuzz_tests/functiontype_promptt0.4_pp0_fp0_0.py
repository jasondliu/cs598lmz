import types
# Test types.FunctionType
def func(): pass
assert type(func) == types.FunctionType

# Test types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType

# Test types.GeneratorType
def gen(): yield 1
assert type(gen()) == types.GeneratorType

# Test types.CodeType
assert type(func.__code__) == types.CodeType

# Test types.TracebackType
try:
    1/0
except:
    tb = sys.exc_info()[2]
    assert type(tb) == types.TracebackType

# Test types.FrameType
def f():
    assert type(sys._getframe()) == types.FrameType
f()

# Test types.GetSetDescriptorType
class C(object):
    def fget(self): return 1
    prop = property(fget)
assert type(C.prop) == types.GetSetDescriptorType

# Test types.MemberDescriptorType
class C(object):
    def fget(self): return 1
    prop = property
