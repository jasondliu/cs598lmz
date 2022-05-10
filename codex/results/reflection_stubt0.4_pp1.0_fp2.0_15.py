fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that the __code__ attribute is not writable
def fn():
    pass

try:
    fn.__code__ = None
except TypeError:
    print("TypeError")
