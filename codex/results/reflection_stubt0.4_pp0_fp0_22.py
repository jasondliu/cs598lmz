fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# __code__ is a read-only attribute
try:
    fn.__code__ = None
except TypeError:
    print("TypeError")

# __code__ must be code object
try:
    fn.__code__ = 1
except TypeError:
    print("TypeError")

# __code__ must be code object
try:
    fn.__code__ = "abc"
except TypeError:
    print("TypeError")

# __code__ must be code object
try:
    fn.__code__ = b"abc"
except TypeError:
    print("TypeError")

# __code__ must be code object
try:
    fn.__code__ = lambda: None
except TypeError:
    print("TypeError")

# __code__ must be code object
try:
    fn.__code__ = (i for i in ())
except TypeError:
    print("TypeError")
