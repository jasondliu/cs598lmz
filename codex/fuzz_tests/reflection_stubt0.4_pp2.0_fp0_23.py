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
    raise Exception("expected TypeError")

# Test that we can't set __code__ to a code object with the wrong type
try:
    fn.__code__ = (lambda: None).__code__
except TypeError:
    pass
else:
    raise Exception("expected TypeError")

# Test that we can't set __code__ to a code object with the wrong number of
# arguments
try:
    fn.__code__ = (lambda x, y: None).__code__
except ValueError:
    pass
else:
    raise Exception("expected ValueError")

# Test that we can't set __code__ to a code object with the wrong number of
# locals
try:
    fn.__code__ = (lambda: None).__code__.replace(b"\x00\x00\x00\x00", b"\x00\x00\x00\x01
