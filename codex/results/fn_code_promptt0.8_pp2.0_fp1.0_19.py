fn = lambda: None
# Test fn.__code__.__hash__() works when __code__ is NULL.
fn.__code__ = None
hash(fn.__code__)

# Make sure we can call __sizeof__ on it, and it doesn't crash.
fn.__sizeof__()

# __sizeof__ is in the method cache. Check that it doesn't crash.
sys.getrefcount(fn)

# Test calling user-provided __sizeof__
class A:
    def __sizeof__(self):
        # Arbitrary number of unique objects for reference counting
        # purposes
        return 1234567890

# This shouldn't crash
sys.getrefcount(A())

# Missing __sizeof__ gives an error
class B:
    pass

try:
    sys.getrefcount(B())
except TypeError:
    pass
else:
    raise Exception

# Cannot pass keyword args
try:
    sys.getrefcount(A(), foo=1)
except TypeError:
    pass
else:
    raise Exception

# Cannot pass non-keyword args
try:
    sys
