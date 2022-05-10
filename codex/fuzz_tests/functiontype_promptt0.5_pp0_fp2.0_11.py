import types
# Test types.FunctionType
assert isinstance(lambda x: x, types.FunctionType)
# Test types.LambdaType
assert isinstance(lambda x: x, types.LambdaType)


# Test that we can nest lambdas
def f():
    return lambda x: lambda y: x + y

assert f()(2)(3) == 5


# Test that we can nest lambdas
def f():
    return lambda x: lambda y: x + y

assert f()(2)(3) == 5


# Test that we can nest lambdas
def f():
    return lambda x: lambda y: x + y

assert f()(2)(3) == 5


# Test that we can nest lambdas
def f():
    return lambda x: lambda y: x + y

assert f()(2)(3) == 5


# Test that we can nest lambdas
def f():
    return lambda x: lambda y: x + y

assert f()(2)(3) == 5


# Test that we can nest lambdas
def f():
    return lambda
