fn = lambda: None
# Test fn.__code__
fn.__code__
try:
    fn.__code__ = fn.__code__
except TypeError:
    print("TypeError")

# Test fn.__closure__
fn.__closure__
try:
    fn.__closure__ = fn.__closure__
except TypeError:
    print("TypeError")
