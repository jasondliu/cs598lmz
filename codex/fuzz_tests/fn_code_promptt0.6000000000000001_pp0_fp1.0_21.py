fn = lambda: None
# Test fn.__code__.co_varnames

def f(x, y, z):
    return 42

assert f.__code__.co_varnames == ("x", "y", "z")
assert f.__code__.co_argcount == 3

# Test fn.__code__.co_filename

def f():
    return 42

assert f.__code__.co_filename == __file__

# Test fn.__code__.co_name

def f():
    return 42

assert f.__code__.co_name == "f"

# Test fn.__code__.co_nlocals

def f():
    x = 1
    y = 2
    return x + y

assert f.__code__.co_nlocals == 2

# Test fn.__code__.co_firstlineno

def f():
    return 42

assert f.__code__.co_firstlineno == 6

# Test fn.__code__.co_lnotab

def f():
    return 42

assert f
