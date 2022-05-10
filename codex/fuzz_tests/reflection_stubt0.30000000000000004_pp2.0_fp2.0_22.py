fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# __code__ is a read-only attribute
try:
    fn.__code__ = None
except TypeError:
    print("TypeError")

# __code__ must be a code object
try:
    fn.__code__ = 42
except TypeError:
    print("TypeError")

# __code__ must be a code object
try:
    fn.__code__ = "not a code object"
except TypeError:
    print("TypeError")

# __code__ must be a code object
try:
    fn.__code__ = b"not a code object"
except TypeError:
    print("TypeError")

# __code__ must be a code object
try:
    fn.__code__ = bytearray(b"not a code object")
except TypeError:
    print("TypeError")

# __code__ must be a code object
try:
    fn.__code__ = memoryview(b"not a code object")
except TypeError:
    print("TypeError")

# __code__ must be
