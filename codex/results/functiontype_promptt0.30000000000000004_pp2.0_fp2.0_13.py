import types
# Test types.FunctionType
def func():
    pass

print(type(func))
print(type(lambda x: x))
print(type(lambda x, y: x + y))
print(type(lambda: None))

# Test types.LambdaType
print(type(lambda: None))

# Test types.GeneratorType
def gen():
    yield 1

print(type(gen))
print(type(gen()))

# Test types.CodeType
def code():
    pass

print(type(code.__code__))

# Test types.TracebackType
try:
    raise Exception()
except Exception as e:
    print(type(e.__traceback__))

# Test types.FrameType
def frame():
    pass

print(type(frame.__code__.co_frame))

# Test types.BuiltinFunctionType
print(type(abs))
print(type(all))
print(type(any))
print(type(ascii))
print(type(bin))
print(type(bool))
print(type(by
