fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test that we can't set __code__ to a non-code object
try:
    fn.__code__ = None
except TypeError:
    pass
else:
    raise Exception("shouldn't be able to set __code__ to a non-code object")

# test that we can't set __code__ to a code object with a different number of
# arguments
try:
    fn.__code__ = (lambda x: None).__code__
except TypeError:
    pass
else:
    raise Exception("shouldn't be able to set __code__ to a code object with a different number of arguments")

# test that we can't set __code__ to a code object with a different number of
# local variables
try:
    fn.__code__ = (lambda: None).__code__
except TypeError:
    pass
else:
    raise Exception("shouldn't be able to set __code__ to a code object with a different number of local variables")

# test that we can't set __code__ to a code object with a different number of
# stack
