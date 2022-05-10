fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #5: A function with a __code__ attribute that is not a code object
# should raise a TypeError.
fn = lambda: None
fn.__code__ = 'foo'
try:
    fn()
except TypeError:
    pass
else:
    raise Exception('TypeError not raised')

# Issue #6: A function with a __code__ attribute that is a code object
# with an invalid co_argcount should raise a ValueError.
fn = lambda: None
fn.__code__ = type(fn.__code__)(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'')
try:
    fn()
except ValueError:
    pass
else:
    raise Exception('ValueError not raised')

# Issue #7: A function with a __code__ attribute that is a code object
# with an invalid co_flags should raise a ValueError.
fn = lambda: None
fn.__code__ = type(fn.__code__)(0, 0, 0, 0, b'', (), (), (), '
