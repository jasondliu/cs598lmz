import types
# Test types.FunctionType
def func(): pass
print type(func) == types.FunctionType
print type(lambda x: x) == types.FunctionType
print type(lambda x: x) == types.LambdaType

# Test types.MethodType
class C(object):
    def method(self): pass
print type(C.method) == types.MethodType
print type(C().method) == types.MethodType

# Test types.BuiltinFunctionType
print type(len) == types.BuiltinFunctionType
print type(len) == types.BuiltinMethodType

# Test types.BuiltinMethodType
print type([].append) == types.BuiltinMethodType

# Test types.ModuleType
import sys
print type(sys) == types.ModuleType

# Test types.TracebackType
try:
    raise Exception
except:
    import sys
    print type(sys.exc_info()[2]) == types.TracebackType

# Test types.FrameType
def f():
    import sys
    return sys._getframe()
print type(f()) == types.Frame
