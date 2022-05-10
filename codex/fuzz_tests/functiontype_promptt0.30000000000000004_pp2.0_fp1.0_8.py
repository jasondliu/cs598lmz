import types
# Test types.FunctionType
def func():
    pass

print(type(func) == types.FunctionType)

# Test types.LambdaType
print(type(lambda: None) == types.LambdaType)

# Test types.GeneratorType
def gen():
    yield 1

g = gen()
print(type(g) == types.GeneratorType)

# Test types.CodeType
print(type(func.__code__) == types.CodeType)

# Test types.TracebackType
try:
    raise Exception()
except:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print(type(exc_traceback) == types.TracebackType)

# Test types.FrameType
def foo():
    return sys._getframe()

print(type(foo()) == types.FrameType)

# Test types.BuiltinFunctionType
print(type(len) == types.BuiltinFunctionType)

# Test types.BuiltinMethodType
print(type([].append) == types.BuiltinMethodType
