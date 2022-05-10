import types
# Test types.FunctionType
__name__ = 'types_function'

def func(x, y):
    return x + y

print(func(1, 3))

# It must be a function
def func2(x):
    return x

print(func2(func))

# It must be a function
func3 = func
print(func3(1, 2))

# Function can be passed as argument
def func4(f, x):
    return f(x)

print(func4(func2, func))

# Function can be returned as result
def func5(x):
    def f(y):
        return x + y
    return f

print(func5(1)(2))

# Function can be nested
def func6(x):
    def f(y):
        def g(z):
            return x + y + z
        return g
    return f

print(func6(1)(2)(3))

# Function can be nested
def func7(x):
    def f(y):
        def g(z):
            return
