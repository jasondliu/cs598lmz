import types
# Test types.FunctionType
def f(): pass
assert type(f) == types.FunctionType
assert type(lambda: None) == types.FunctionType
assert type(int) == types.BuiltinFunctionType
assert type(list.append) == types.BuiltinMethodType
assert type(str.split) == types.MethodType

# Test types.LambdaType
assert type(lambda: None) == types.LambdaType

# Test types.GeneratorType
assert type((lambda: (yield))()) == types.GeneratorType

# Test types.CodeType
def f(): pass
assert type(f.__code__) == types.CodeType

# Test types.FrameType
def f():
    g()
def g():
    import sys
    return sys._getframe()
assert type(g()) == types.FrameType

# Test types.TracebackType
def f():
    1/0
try:
    f()
except ZeroDivisionError:
    tb = sys.exc_info()[2]
assert type(tb) == types.TracebackType


