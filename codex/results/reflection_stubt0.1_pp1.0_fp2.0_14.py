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

# Test that we can't set __code__ to a code object with a different number of
# arguments
def fn():
    pass

try:
    fn.__code__ = (lambda x: None).__code__
except TypeError:
    pass
else:
    raise Exception("Should have raised TypeError")

# Test that we can't set __code__ to a code object with a different number of
# locals
def fn():
    pass

try:
    fn.__code__ = (lambda: None).__code__
except TypeError:
    pass
else:
    raise Exception("Should have raised TypeError")

# Test that we can't set __code__ to a code object with a different number of
# stack items
def fn():
    pass

try:
    fn.__code__
