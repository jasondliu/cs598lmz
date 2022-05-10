import types
# Test types.FunctionType
def f():
    pass

assert type(f) == types.FunctionType

# Test types.LambdaType
g = lambda x: x
assert type(g) == types.LambdaType

# Test types.GeneratorType
def h():
    yield 1

assert type(h()) == types.GeneratorType

# Test types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType

# Test types.BuiltinMethodType
assert type([].append) == types.BuiltinMethodType

# Test types.MethodType
class A:
    def f(self):
        pass

assert type(A().f) == types.MethodType

# Test types.ModuleType
assert type(types) == types.ModuleType

# Test types.TracebackType
try:
    raise Exception
except Exception:
    import sys
    assert type(sys.exc_info()[2]) == types.TracebackType

# Test types.FrameType
assert type(sys._getframe()) == types.FrameType

# Test types.
