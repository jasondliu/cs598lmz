import types
# Test types.FunctionType
def foo():
    pass

f = foo
print(type(f) is types.FunctionType)
print(type(f) == types.FunctionType)

# Test types.BuiltinFunctionType
print(type(abs) is types.BuiltinFunctionType)
print(type(abs) == types.BuiltinFunctionType)

# Test types.LambdaType
g = lambda x: x+1
print(type(g) is types.LambdaType)
print(type(g) == types.LambdaType)

# Test types.GeneratorType
def bar():
    yield 1
b = bar()
print(type(b) is types.GeneratorType)
print(type(b) == types.GeneratorType)

# Test types.TracebackType
try:
    raise Exception
except Exception as e:
    print(type(e.__traceback__) is types.TracebackType)
    print(type(e.__traceback__) == types.TracebackType)

# Test types.FrameType
def f():

