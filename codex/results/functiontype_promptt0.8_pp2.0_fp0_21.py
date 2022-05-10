import types
# Test types.FunctionType where argc can be between 0 and 3:

# Number of arguments
def f():
    return 0
def f(x):
    return 1
def f(x,y):
    return 2
def f(x,y,z):
    return 3

# Test all combinations of arguments
assert f() == 0
assert f(1) == 1
assert f(1,2) == 2
assert f(1,2,3) == 3

# Same thing, as keyword arguments
# (all combinations of arguments must also work with keyword arguments)
assert f() == 0
assert f(x=1) == 1
assert f(y=2) == 0
assert f(x=1,y=2) == 2
assert f(x=1,z=3) == 1
assert f(x=1,y=2,z=3) == 3
assert f(y=2,z=3) == 1
assert f(y=2,z=3,x=1) == 3

# Test all combinations of keyword arguments and non-keyword arguments
assert f(1,y=2
