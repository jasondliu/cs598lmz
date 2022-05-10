import types
# Test types.FunctionType

def function_caller(f, a, b, c):
    if not isinstance(f, types.FunctionType):
        raise TypeError("parameter f must be a function")
    return f(a, b, c)

def foo(a, b, c):
    print("a = {}, b = {}, c = {}".format(a, b, c))
    return None

f = lambda a, b, c: a + b + c

print(function_caller(foo, 1, 2, 3))
print(function_caller(f, 1, 2, 3))

# Check input type
print(function_caller(1, 2, 3, 4))


# Test types.LambdaType
def function_caller2(f):
    if not isinstance(f, types.LambdaType):
        raise TypeError("parameter f must be a function")
    return f

f = lambda x, y: x + y
print(function_caller2(f)(1, 2))
g = lambda x, y, z
