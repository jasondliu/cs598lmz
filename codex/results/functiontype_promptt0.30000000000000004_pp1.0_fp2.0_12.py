import types
# Test types.FunctionType
def f():
    pass

assert type(f) == types.FunctionType
# Test types.LambdaType
g = lambda x: x

assert type(g) == types.LambdaType
# Test types.GeneratorType
def gen():
    yield 1

assert type(gen()) == types.GeneratorType
# Test types.CodeType
def f():
    pass

assert type(f.__code__) == types.CodeType
# Test types.TracebackType
try:
    1/0
except ZeroDivisionError as e:
    tb = e.__traceback__

assert type(tb) == types.TracebackType
# Test types.FrameType
def f():
    pass

assert type(f.__code__.co_frame) == types.FrameType
# Test types.BuiltinFunctionType
assert type(abs) == types.BuiltinFunctionType
# Test types.BuiltinMethodType
assert type(abs) == types.BuiltinFunctionType
# Test types.ModuleType
assert type(types) == types.Module
