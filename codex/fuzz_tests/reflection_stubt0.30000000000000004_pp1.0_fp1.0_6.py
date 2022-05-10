fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that a generator function with a non-generator code object
# raises a TypeError.
fn = lambda: None
fn.__code__ = lambda: None
try:
    fn()
except TypeError:
    pass
else:
    raise Exception("TypeError not raised")

# Test that a generator function with a non-generator code object
# raises a TypeError.
fn = lambda: None
fn.__code__ = lambda: None
try:
    fn()
except TypeError:
    pass
else:
    raise Exception("TypeError not raised")

# Test that a generator function with a non-generator code object
# raises a TypeError.
fn = lambda: None
fn.__code__ = lambda: None
try:
    fn()
except TypeError:
    pass
else:
    raise Exception("TypeError not raised")

# Test that a generator function with a non-generator code object
# raises a TypeError.
fn = lambda: None
fn.__code__ = lambda: None
try:
    fn()
except Type
