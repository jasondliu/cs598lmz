import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType
assert type(f) is types.BuiltinFunctionType
assert type(f) is types.BuiltinMethodType

# Test types.LambdaType
g = lambda: None
assert type(g) is types.LambdaType

# Test types.GeneratorType
def h(): yield
assert type(h()) is types.GeneratorType

# Test types.CodeType
assert type(h.__code__) is types.CodeType

# Test types.TracebackType
try:
    1/0
except:
    import sys
    tb = sys.exc_info()[2]
    assert type(tb) is types.TracebackType

# Test types.FrameType
def i():
    assert type(sys._getframe()) is types.FrameType
i()

# Test types.ModuleType
import types
assert type(types) is types.ModuleType

# Test types.GetSetDescriptorType
class C(object):
    def fget(self): pass
   
