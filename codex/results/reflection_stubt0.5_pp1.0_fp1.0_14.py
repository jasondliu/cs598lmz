fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that the interpreter can handle a generator with a __code__ attribute
# that is not a code object.
gi.__code__ = None
try:
    fn()
except TypeError:
    pass
else:
    print("Failed to raise TypeError")

gi.__code__ = "not a code object"
try:
    fn()
except TypeError:
    pass
else:
    print("Failed to raise TypeError")

# Test that the interpreter can handle a generator with a __code__ attribute
# that is a code object with no co_code attribute.
gi.__code__ = type(gi.__code__)
try:
    fn()
except TypeError:
    pass
else:
    print("Failed to raise TypeError")

gi.__code__.co_code = "some bytecode"
try:
    fn()
except TypeError:
    pass
else:
    print("Failed to raise TypeError")

# Test that the interpreter can handle a generator with a __code__ attribute
# that is a code
