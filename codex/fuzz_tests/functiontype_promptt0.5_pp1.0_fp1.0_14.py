import types
# Test types.FunctionType
def f():
    pass
assert type(f) is types.FunctionType

# Test types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType

# Test types.MethodType
class A:
    def f(self):
        pass
assert type(A.f) is types.MethodType
assert type(A().f) is types.MethodType

# Test types.LambdaType
assert type(lambda x: x) is types.LambdaType

# Test types.GeneratorType
def g():
    yield 1
assert type(g()) is types.GeneratorType

# Test types.GeneratorType
class C:
    pass
assert type(C()) is types.InstanceType

# Test types.TracebackType
try:
    raise Exception
except:
    tb = sys.exc_info()[2]
assert type(tb) is types.TracebackType

# Test types.FrameType
def h():
    return sys._getframe()
assert type(h()) is types.FrameType

# Test types
