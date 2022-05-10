fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that we can't set __code__ to a non-code object
try:
    fn.__code__ = None
except TypeError:
    pass
else:
    raise Exception("Shouldn't be able to set __code__ to a non-code object")

# Test that we can't set __code__ to a code object with a different number of
# arguments
try:
    fn.__code__ = (lambda x: None).__code__
except TypeError:
    pass
else:
    raise Exception("Shouldn't be able to set __code__ to a code object with a different number of arguments")

# Test that we can't set __code__ to a code object with a different number of
# locals
try:
    fn.__code__ = (lambda: None).__code__
except TypeError:
    pass
else:
    raise Exception("Shouldn't be able to set __code__ to a code object with a different number of locals")

# Test that we can't set __code__ to a code object with a different number of
# stack items

