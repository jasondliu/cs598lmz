import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType

# Test types.LambdaType
g = lambda: None
assert type(g) is types.LambdaType

# Test types.GeneratorType
def h(): yield 1
assert type(h()) is types.GeneratorType

# Test types.MethodType
class A:
    def m(self): pass
assert type(A().m) is types.MethodType

# Test types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType

# Test types.BuiltinMethodType
assert type([].append) is types.BuiltinMethodType

# Test types.ModuleType
import sys
assert type(sys) is types.ModuleType

# Test types.TracebackType
try:
    raise Exception
except:
    import sys
    tb = sys.exc_info()[2]
    assert type(tb) is types.TracebackType

# Test types.FrameType
def foo():
    frame = sys._getframe()
    assert type(frame)
