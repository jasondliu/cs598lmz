from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, "test", f.__defaults__, f.__closure__))

# Code object of a function.
f.__code__

# Function's globals.
f.__globals__

# Function's default values.
f.__defaults__

# Function's closure.
f.__closure__

# Function's docstring.
f.__doc__

# Function's name.
f.__name__

# Function's module.
f.__module__

# Function's dict.
f.__dict__
