import types
# Test types.FunctionType
def foo():
    pass
f = foo
print(isinstance(f, types.FunctionType))
# Test types.MethodType
def foo():
    pass
f = foo
print(isinstance(f, types.MethodType))
# Test types.BuiltinFunctionType
import math
print(isinstance(math.sin, types.BuiltinFunctionType))
# Test types.BuiltinMethodType
print(isinstance([].append, types.BuiltinMethodType))
# Test types.ModuleType
import math
print(isinstance(math, types.ModuleType))
# Test types.TracebackType
import sys
tb = sys.last_traceback
print(isinstance(tb, types.TracebackType))
# Test types.FrameType
import sys
f = sys._getframe()
print(isinstance(f, types.FrameType))
# Test types.CodeType
def foo(): pass
print(isinstance(foo.__code__, types.CodeType))
# Test types.MethodWrapperType
print(isinstance([].append, types.MethodWrapperType))
