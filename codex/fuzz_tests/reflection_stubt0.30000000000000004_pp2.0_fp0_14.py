fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# Check that we can't set __code__ to a non-code object
try:
    fn.__code__ = None
except TypeError:
    pass
else:
    raise Exception("setting __code__ to a non-code object should have failed")

# Check that we can't set __code__ to a code object with a different number of arguments
try:
    fn.__code__ = type(fn.__code__)(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'')
except ValueError:
    pass
else:
    raise Exception("setting __code__ to a code object with a different number of arguments should have failed")

# Check that we can't set __code__ to a code object with a different number of locals
try:
    fn.__code__ = type(fn.__code__)(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'')
except ValueError:
    pass
else:
    raise Exception("setting __code__ to a code object
