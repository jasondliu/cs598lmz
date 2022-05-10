from types import FunctionType
list(FunctionType(obj).__code__.co_varnames) # get variables in the function
list(FunctionType(obj).__code__.co_names) # get function names
list(FunctionType(obj).__code__.co_consts) # get constants

# Function call
def func(*args, **kwargs):
    pass
func(*[1, 2, 3], **{'a': 1, 'b': 2})

# decorator
def decorator(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper

# get all attributes
dir(obj)

# get all attributes from a class
dir(classname)

# get all attributes from a class
dir(classname)

# list assign
a, b, c = 1, 2, 3

# list assign
a, b, c = 1, 2, 3

# list assign
a, b, c = 1, 2, 3

# list assign
a, b, c = 1, 2, 3

# list assign
a, b, c
