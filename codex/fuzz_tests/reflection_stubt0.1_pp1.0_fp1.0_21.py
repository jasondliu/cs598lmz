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
    raise Exception("Should have raised TypeError")

# Test that we can't set __code__ to a non-code object
try:
    fn.__code__ = 1
except TypeError:
    pass
else:
    raise Exception("Should have raised TypeError")

# Test that we can't set __code__ to a non-code object
try:
    fn.__code__ = "hello"
except TypeError:
    pass
else:
    raise Exception("Should have raised TypeError")

# Test that we can't set __code__ to a non-code object
try:
    fn.__code__ = b"hello"
except TypeError:
    pass
else:
    raise Exception("Should have raised TypeError")

# Test that we can't set __code__ to a non-code object
try:
    fn.__code__ = bytearray(b"hello
