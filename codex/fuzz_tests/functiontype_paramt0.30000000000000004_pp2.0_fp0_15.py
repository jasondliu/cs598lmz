from types import FunctionType
list(FunctionType(lambda x: x + 1, globals(), 'add_one')(1))

# the same as
def add_one(x):
    return x + 1

list(add_one(1))

# the same as
def add_one(x):
    return x + 1

add_one.__name__

# the same as
def add_one(x):
    return x + 1

add_one.__code__

# the same as
def add_one(x):
    return x + 1

add_one.__code__.co_argcount

# the same as
def add_one(x):
    return x + 1

add_one.__code__.co_varnames

# the same as
def add_one(x):
    return x + 1

add_one.__code__.co_argcount

# the same as
def add_one(x):
    return x + 1

add_one.__code__.co_argcount

# the same as
def add_one(
