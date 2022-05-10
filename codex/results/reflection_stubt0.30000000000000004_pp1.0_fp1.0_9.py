fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that we can't create a code object with an invalid co_flags
try:
    types.CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'')
except ValueError:
    pass
else:
    raise RuntimeError("Did not raise ValueError")

# Test that we can't create a code object with an invalid co_argcount
try:
    types.CodeType(-1, 0, 0, 0, b'', (), (), (), '', '', 0, b'')
except ValueError:
    pass
else:
    raise RuntimeError("Did not raise ValueError")

# Test that we can't create a code object with an invalid co_kwonlyargcount
try:
    types.CodeType(0, -1, 0, 0, b'', (), (), (), '', '', 0, b'')
except ValueError:
    pass
else:
    raise RuntimeError("Did not raise ValueError")

# Test that we can't create a code object with an invalid co_nlocals
try:
