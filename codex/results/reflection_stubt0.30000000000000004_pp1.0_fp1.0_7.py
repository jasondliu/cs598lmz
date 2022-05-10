fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that we can't set __code__ to a non-code object
def fn():
    pass

try:
    fn.__code__ = 1
except TypeError:
    pass
else:
    raise Exception("Should have raised TypeError")

# Test that we can't set __code__ to a code object with a different
# number of arguments
def fn(a):
    pass

try:
    fn.__code__ = lambda: None
except ValueError:
    pass
else:
    raise Exception("Should have raised ValueError")

# Test that we can't set __code__ to a code object with a different
# number of locals
def fn():
    a = 1

try:
    fn.__code__ = lambda: None
except ValueError:
    pass
else:
    raise Exception("Should have raised ValueError")

# Test that we can't set __code__ to a code object with a different
# number of stack items
def fn():
    return 1, 2

try:
    fn.__code__ = lambda: None
