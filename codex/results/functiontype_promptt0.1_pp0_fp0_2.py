import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType
assert type(f) is types.BuiltinFunctionType

# Test types.MethodType
class C:
    def m(self): pass
assert type(C.m) is types.MethodType
assert type(C().m) is types.MethodType

# Test types.BuiltinMethodType
assert type(list.append) is types.BuiltinMethodType
assert type([].append) is types.BuiltinMethodType

# Test types.ModuleType
import sys
assert type(sys) is types.ModuleType

# Test types.TracebackType
try:
    raise Exception
except:
    tb = sys.exc_info()[2]
    assert type(tb) is types.TracebackType

# Test types.FrameType
def g():
    assert type(sys._getframe()) is types.FrameType
g()

# Test types.CodeType
assert type(g.__code__) is types.CodeType

# Test types.GeneratorType
def h():
    yield 1
