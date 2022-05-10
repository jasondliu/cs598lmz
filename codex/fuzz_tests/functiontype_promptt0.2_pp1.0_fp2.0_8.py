import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)

# Test types.MethodType
class A:
    def f(self):
        pass

a = A()
assert isinstance(a.f, types.MethodType)

# Test types.BuiltinMethodType
assert isinstance(a.__hash__, types.BuiltinMethodType)

# Test types.ModuleType
assert isinstance(types, types.ModuleType)

# Test types.TracebackType
try:
    raise Exception
except:
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.TracebackType)

# Test types.FrameType
def g():
    return sys._getframe()

assert isinstance(g(), types.FrameType)

# Test types.CodeType
assert isinstance(f.__code__, types.CodeType)

# Test types.GeneratorType
def h():

