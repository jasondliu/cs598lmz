import types
# Test types.FunctionType, types.MethodType

def f():
    pass

class C:
    def g(self):
        pass

assert type(f) is types.FunctionType
assert type(C.g) is types.MethodType
assert type(C().g) is types.MethodType

# Test types.BuiltinFunctionType

assert type(len) is types.BuiltinFunctionType

# Test types.BuiltinMethodType

assert type([].append) is types.BuiltinMethodType

# Test types.ModuleType

import sys
assert type(sys) is types.ModuleType

# Test types.TracebackType

try:
    raise ValueError
except:
    tb = sys.exc_info()[2]
    assert type(tb) is types.TracebackType

# Test types.FrameType

def f():
    return sys._getframe()
assert type(f()) is types.FrameType

# Test types.CodeType

def f():
    pass
assert type(f.__code__) is types.CodeType

#
