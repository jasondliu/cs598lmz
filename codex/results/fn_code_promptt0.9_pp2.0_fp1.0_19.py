fn = lambda: None
# Test fn.__code__
fn.__code__ = 3
try:
    fn.__code__ = None
except TypeError:
    print("TypeError")
