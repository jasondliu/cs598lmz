fn = lambda: None
# Test fn.__code__.__ dict.__code__.__
if not hasattr(fn, '__code__'):
    raise AttributeError

try:
    fn.__code__.__
except TypeError:
    pass
