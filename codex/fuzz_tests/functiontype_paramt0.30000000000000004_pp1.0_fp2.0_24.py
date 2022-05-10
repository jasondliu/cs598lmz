from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# This is a list of all the variable names in the function.
# The first is the name of the function itself, the second is the first argument, etc.

# We can use this to get the names of the arguments of a function.
def f(a, b, c):
    pass

list(FunctionType(f.__code__, {}).__code__.co_varnames)

# We can also use this to get the names of the local variables in a function.
def f(a, b, c):
    d = 1
    e = 2
    f = 3

list(FunctionType(f.__code__, {}).__code__.co_varnames)

# If we want to get the names of the local variables in a function, we have to do a little more work.
# We have to get the names of the local variables in the function,
# and then remove the names of the arguments from that list.
def f(a, b, c):
    d = 1
    e =
