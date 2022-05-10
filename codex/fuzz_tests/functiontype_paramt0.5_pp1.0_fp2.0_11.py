from types import FunctionType
list(FunctionType(FunctionType.__code__, globals(), 'func', FunctionType.__defaults__, FunctionType.__closure__))

# code object
import dis
dis.dis(FunctionType)

# code object attributes
import inspect
print(inspect.getmembers(FunctionType.__code__))

# function attributes
print(inspect.getmembers(FunctionType))

# function globals
print(inspect.getmembers(FunctionType.__globals__))

# function default arguments
print(inspect.getmembers(FunctionType.__defaults__))

# function closure
print(inspect.getmembers(FunctionType.__closure__))

# function doc
print(inspect.getmembers(FunctionType.__doc__))

# function name
print(inspect.getmembers(FunctionType.__name__))

# function module
print(inspect.getmembers(FunctionType.__module__))

# function dict
print(inspect.getmembers(FunctionType.__dict__))

# function annotations
print(inspect.getmembers(FunctionType.
