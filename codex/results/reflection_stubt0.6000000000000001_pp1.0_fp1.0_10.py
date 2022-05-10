fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# This should raise a TypeError, but it currently raises a SystemError.
# See issue #19276.
fn = lambda: None
fn.__code__ = gi
fn()

# Check that a code object can be made into a function.
def f():
    pass
f2 = types.FunctionType(f.__code__, f.__globals__, "f2", (), f.__closure__)
assert f2() is None

# Check that a code object with a non-tuple closure can be made into a function.
def f():
    x = 3
    def g():
        return x
    return g

g1 = f()
g2 = types.FunctionType(g1.__code__, g1.__globals__, "g2", (), g1.__closure__)
assert g2() == 3

# Check that a code object with a tuple closure can be made into a function.
def f():
    x = 3
    y = 4
    def g():
        return x + y
