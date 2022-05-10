fn = lambda: None
# Test fn.__code__.co_argcount

def f(a, *b):
    fn.__code__.co_argcount

# Test fn.__code__.co_filename

def f(a, *b):
    fn.__code__.co_filename

# Test fn.__code__.co_varnames

def f(a, *b):
    fn.__code__.co_varnames

# Test inspect.getfullargspec()

def f():
    inspect.getfullargspec(fn)

# Test fn.__code__.co_flags (should not trigger interpreter crash).

def f():
    flags = fn.__code__.co_flags

# Test inspect.formatargspec(), inspect.formatargvalues()

def f():
    inspect.formatargspec(fn)
    inspect.formatargvalues(fn)

def simple_function(a: int):
    return a

# FEATURE: Pickling

# This is not a test case, just a placeholder to make sure that unpickling is
# tested during CI.
