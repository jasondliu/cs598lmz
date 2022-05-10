from types import FunctionType
list(FunctionType(f.__code__, globals(), "foo"))

# Code objects can be inspected to get information about the code
# they represent.

# How many arguments does the function take?
f.__code__.co_argcount

# What are the names of the local variables?
f.__code__.co_varnames

# What kind of code object is this?
f.__code__.co_name

# What is the name of the file in which the code object was defined?
f.__code__.co_filename

# What is the first line number of the function?
f.__code__.co_firstlineno

# What kind of object is this?
type(f)

# What is its name?
f.__name__

# What is its docstring?
f.__doc__

# What is the module in which it was defined?
f.__module__

# What is its default argument?
f.__defaults__

# What is the dictionary of its attributes?
f.__dict__

# What is the dictionary of
