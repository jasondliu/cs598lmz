fn = lambda: None
# Test fn.__code__.co_argcount
fn()  # It indeed has no arguments.
WARNING: Not listing arguments of a function that is already called.
fn()  # Again, it has no arguments.

# Now, turn on the warning.
logit.warning_if_called = True
fn()  # The first call to called function does not trigger the warning.
fn()  # This call triggers the warning.
WARNING: Not listing arguments of a function that is already called.
fn()  # Again, no warning.

# Wether it works or not, gc.collect() is not a pure function.
cpdef func():
    gc.collect()
    return 0
 
def func2():
    gc.collect()
    return 0

%timeit func()
%timeit func()
%timeit func()

%timeit func2()
%timeit func2()
%timeit func2() 
 
d = {}

def f():
    """Returns True iff x is in d"""
    return 'x' in d

%timeit f()
%timeit f
