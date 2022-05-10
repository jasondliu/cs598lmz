fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# This should fail with a TypeError
try:
    fn.__code__ = 1
except TypeError:
    print("TypeError")

# This should fail with a TypeError
try:
    fn.__code__ = "abc"
except TypeError:
    print("TypeError")

# This should fail with a TypeError
try:
    fn.__code__ = b"abc"
except TypeError:
    print("TypeError")

# This should fail with a TypeError
try:
    fn.__code__ = bytearray(b"abc")
except TypeError:
    print("TypeError")

# This should fail with a TypeError
try:
    fn.__code__ = memoryview(b"abc")
except TypeError:
    print("TypeError")

# This should fail with a TypeError
try:
    fn.__code__ = range(10)
except TypeError:
    print("TypeError")

# This should fail with a TypeError
try:
    fn.__code__ = [1,
