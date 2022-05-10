fn = lambda: None
# Test fn.__code__
setattr(fn, "__code__", 42)
try:
    fn.__code__
except TypeError:
    print("TypeError")

# Test fn.__defaults__
setattr(fn, "__defaults__", 42)
try:
    fn.__defaults__
except TypeError:
    print("TypeError")

# Test fn.__globals__
setattr(fn, "__globals__", 42)
try:
    fn.__globals__
except TypeError:
    print("TypeError")

# Test fn.__name__
setattr(fn, "__name__", 42)
try:
    fn.__name__
except TypeError:
    print("TypeError")

# Test fn.__qualname__
setattr(fn, "__qualname__", 42)
try:
    fn.__qualname__
except TypeError:
    print("TypeError")
