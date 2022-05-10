from types import FunctionType
list(FunctionType(FunctionType.__code__).__code__.co_varnames)

# ['x']

# Use the inspect module to get the names of the parameters.
import inspect

def foo():
    pass

print(inspect.getargspec(foo))

# ArgSpec(args=[], varargs=None, keywords=None, defaults=None)

# Use the inspect module to get the names of the parameters of a lambda function
import inspect

my_func = lambda x: x

print(inspect.getargspec(my_func))

# ArgSpec(args=['x'], varargs=None, keywords=None, defaults=None)

# Use the inspect module to get the names of the parameters of a function that receives a variable number of arguments
import inspect

my_func = lambda *args: args

print(inspect.getargspec(my_func))

# ArgSpec(args=['args'], varargs='args', keywords=None, defaults=None)

# Use the inspect module to get the names of the parameters of a function that receives keyword arguments

