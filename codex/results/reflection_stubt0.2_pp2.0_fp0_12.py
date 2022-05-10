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
    print("Shouldn't be able to set __code__ to a non-code object")

# Test that we can't set __code__ to a code object with the wrong number of
# arguments
try:
    fn.__code__ = type(fn.__code__)(0, 0, 0, 0, b'', (), (), '', '', 0, b'')
except ValueError:
    pass
else:
    print("Shouldn't be able to set __code__ to a code object with the wrong number of arguments")

# Test that we can't set __code__ to a code object with the wrong number of
# locals
try:
    fn.__code__ = type(fn.__code__)(0, 0, 0, 0, b'', (), (), '', '', 0, b'')
except ValueError:
    pass
else:
    print("Shouldn't be able to set
