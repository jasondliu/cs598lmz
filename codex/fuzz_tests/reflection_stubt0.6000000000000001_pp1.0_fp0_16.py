fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
try:
    fn()
except TypeError:
    pass
else:
    print("expected TypeError")

# Test that the exception raised is a TypeError and not a ValueError
try:
    fn.__code__ = 0
except TypeError:
    pass
else:
    print("expected TypeError")

# Test that the exception raised is a TypeError and not a ValueError
try:
    fn.__code__ = "this is not a code object"
except TypeError:
    pass
else:
    print("expected TypeError")

# Test that the exception raised is a TypeError and not a ValueError
try:
    fn.__code__ = fn
except TypeError:
    pass
else:
    print("expected TypeError")
