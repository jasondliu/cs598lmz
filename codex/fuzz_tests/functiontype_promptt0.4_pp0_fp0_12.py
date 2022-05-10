import types
# Test types.FunctionType
def f():
    pass

if type(f) == types.FunctionType:
    print("f is a function")
else:
    print("f is not a function")

# Test types.LambdaType
g = lambda x: x**2
if type(g) == types.LambdaType:
    print("g is a lambda function")
else:
    print("g is not a lambda function")

# Test types.GeneratorType
def h():
    yield 1
    yield 2

if type(h) == types.GeneratorType:
    print("h is a generator function")
else:
    print("h is not a generator function")

# Test types.BuiltinFunctionType
if type(len) == types.BuiltinFunctionType:
    print("len is a builtin function")
else:
    print("len is not a builtin function")

# Test types.BuiltinMethodType
if type([].append) == types.BuiltinMethodType:
    print("append is a builtin method")
else:
    print("append is not a
