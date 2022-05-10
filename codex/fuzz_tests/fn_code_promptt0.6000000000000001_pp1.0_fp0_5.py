fn = lambda: None
# Test fn.__code__
setattr(fn, '__code__', 42)
try:
    fn.__code__ = 42
except TypeError:
    pass
else:
    raise RuntimeError
# Test fn.__code__.co_code
setattr(fn.__code__, 'co_code', 42)
try:
    fn.__code__.co_code = 42
except TypeError:
    pass
else:
    raise RuntimeError
# Test fn.__code__.co_consts
setattr(fn.__code__, 'co_consts', 42)
try:
    fn.__code__.co_consts = 42
except TypeError:
    pass
else:
    raise RuntimeError
# Test fn.__code__.co_names
setattr(fn.__code__, 'co_names', 42)
try:
    fn.__code__.co_names = 42
except TypeError:
    pass
else:
    raise RuntimeError
# Test fn.__code__.co_varnames
setattr(fn.__code__, 'co_v
