import types
# Test types.FunctionType
if isinstance(pow, types.FunctionType):
    print("pow is built-in function")

# Test types.LambdaType
if isinstance(lambda x: x, types.LambdaType):
    print("lambda is a lambda function")

# Test types.GeneratorType
x = (x * x for x in range(10))
if isinstance(x, types.GeneratorType):
    print("x is a generator")

# Test types.GeneratorType
x = [x * x for x in range(10)]
if isinstance(x, types.GeneratorType):
    print("x is not a generator")

# Test types.TracebackType
try:
    raise TypeError
except TypeError as e:
    if isinstance(e.__traceback__, types.TracebackType):
        print("e.__traceback__ is a traceback")

# Test types.CodeType
def foo(): pass
if isinstance(foo.__code__, types.CodeType):
    print("foo.__code__ is a code")
