fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
try:
    fn()
except TypeError:
    pass
else:
    raise Exception("didn't raise TypeError")

# this one is not allowed in CPython:
# (lambda: None).__code__ = (i for i in ())

# this one is not allowed in PyPy:
# (i for i in ()).__code__ = lambda: None

# check that we can't set __code__ to a bad value
try:
    fn.__code__ = None
except TypeError:
    pass
else:
    raise Exception("didn't raise TypeError")

# check that we can't delete __code__
try:
    del fn.__code__
except TypeError:
    pass
else:
    raise Exception("didn't raise TypeError")

# check that we can't set __code__ on a built-in function
try:
    open.__code__ = None
except TypeError:
    pass
else:
    raise Exception("didn't raise TypeError")

# check that we can't set __code__ on a built-in method
try
