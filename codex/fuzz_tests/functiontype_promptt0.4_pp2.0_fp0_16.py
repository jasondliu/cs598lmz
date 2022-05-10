import types
# Test types.FunctionType
def f():
    pass
assert type(f) is types.FunctionType

# Test types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType

# Test types.MethodType
class C:
    def m(self):
        pass
assert type(C.m) is types.MethodType

# Test types.BuiltinMethodType
assert type([].append) is types.BuiltinMethodType

# Test types.ModuleType
import sys
assert type(sys) is types.ModuleType

# Test types.TracebackType
import sys
def f():
    raise Exception
try:
    f()
except:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    assert type(exc_traceback) is types.TracebackType

# Test types.FrameType
import sys
def f():
    g()
def g():
    h()
def h():
    i = sys._getframe()
assert type(i) is types.FrameType

# Test types.CodeType
def f(): pass
