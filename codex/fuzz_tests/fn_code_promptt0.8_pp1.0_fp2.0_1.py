fn = lambda: None
# Test fn.__code__
try:
    fn.__code__
except AttributeError:
    print("SKIP")
    raise SystemExit

# Test on a simple function
def f():
    pass

c = f.__code__

assert c.co_argcount == 0
assert list(c.co_varnames) == ['f']
assert list(c.co_cellvars) == []
assert list(c.co_freevars) == []
assert hasattr(c, "co_code")

# Test on a function with arguments
def f1(a):
    pass

c = f1.__code__

assert c.co_argcount == 1
assert list(c.co_varnames) == ['a', 'f1']
assert list(c.co_cellvars) == []
assert list(c.co_freevars) == []

# Test on a function with default values
def f(a=1):
    pass

c = f.__code__

assert c.co_argcount == 1
assert list(c.co
