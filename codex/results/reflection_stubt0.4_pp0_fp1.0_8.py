fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# Test the case where the code object is not a code object.
try:
    fn.__code__ = None
except TypeError:
    pass
else:
    print("Expected TypeError")

# Test the case where the code object is a code object, but not a
# function's code object.
try:
    fn.__code__ = gi.__code__
except TypeError:
    pass
else:
    print("Expected TypeError")

# Test the case where the code object is a function's code object, but
# the function is not a function.
try:
    fn.__code__ = gi.__code__
except TypeError:
    pass
else:
    print("Expected TypeError")

# Test the case where the code object is a function's code object, but
# the function is not a function.
try:
    fn.__code__ = gi.__code__
except TypeError:
    pass
else:
    print("Expected TypeError")

# Test the case where the code object is a function's code
