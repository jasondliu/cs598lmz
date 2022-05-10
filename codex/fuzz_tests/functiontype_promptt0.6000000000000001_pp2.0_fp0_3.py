import types
# Test types.FunctionType
def func():
    pass

assert(isinstance(func, types.FunctionType))

# Test types.MethodType
class Foo():
    def meth():
        pass

assert(isinstance(Foo.meth, types.MethodType))

# Test types.BuiltinFunctionType
assert(isinstance(len, types.BuiltinFunctionType))

# Test types.BuiltinMethodType
assert(isinstance([].append, types.BuiltinMethodType))

# Test types.ModuleType
import sys
assert(isinstance(sys, types.ModuleType))

# Test types.TracebackType
try:
    raise Exception()
except:
    etype, evalue, etraceback = sys.exc_info()
    assert(isinstance(etype, types.ClassType))
    assert(isinstance(evalue, types.InstanceType))
    assert(isinstance(etraceback, types.TracebackType))

# Test types.FrameType
def foo():
    return sys._getframe()
assert(isinstance(foo(), types.FrameType))

