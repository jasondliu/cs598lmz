fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that we can't assign to __code__
def fn():
    pass

try:
    fn.__code__ = None
except TypeError:
    print("TypeError")

# Test that we can't assign to __code__
def fn():
    pass

try:
    fn.__code__ = 1
except TypeError:
    print("TypeError")

# Test that we can't assign to __code__
def fn():
    pass

try:
    fn.__code__ = "abc"
except TypeError:
    print("TypeError")

# Test that we can't assign to __code__
def fn():
    pass

try:
    fn.__code__ = b"abc"
except TypeError:
    print("TypeError")

# Test that we can't assign to __code__
def fn():
    pass

try:
    fn.__code__ = bytearray(b"abc")
except TypeError:
    print("TypeError")

# Test that we can't assign to __code
