fn = lambda: None
# Test fn.__code__
setattr(fn, '__code__', 'test_fn1')
try:
    fn()
except TypeError:
    pass

setattr(fn, '__code__', b'test_fn2')
try:
    fn()
except TypeError:
    pass

# Test fn.__dict__
setattr(fn, '__dict__', 'test_fn1')
try:
    fn()
except TypeError:
    pass

setattr(fn, '__dict__', b'test_fn2')
try:
    fn()
except TypeError:
    pass

# Test fn.__name__
setattr(fn, '__name__', 'test_fn1')
try:
    fn()
except TypeError:
    pass

setattr(fn, '__name__', b'test_fn2')
try:
    fn()
except TypeError:
    pass

# Test fn.__qualname__
setattr(fn, '__qualname__', 'test_fn1')
try:
    fn()
except TypeError
