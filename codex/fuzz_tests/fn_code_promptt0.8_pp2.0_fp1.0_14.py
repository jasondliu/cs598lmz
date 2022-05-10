fn = lambda: None
# Test fn.__code__.co_flags & 0b00000010100000000 (no generator support)
setattr(fn, '__code__', type(fn.__code__)(*map(
    lambda x: 0, range(1, 8)
)))

# Test fn.__closure__ is None
setattr(fn, '__closure__', None)

# Test whether sys.flags.graalpython_co_flags_ignore_mask can override
# the above checks, allowing flags to be ignored.
setattr(fn, '__code__', type(fn.__code__)(*map(
    lambda x: 0b00000010100000000, range(1, 8)
)))

setattr(fn, '__closure__', (1,2,3))
if sys.flags.graalpython_co_flags_ignore_mask:
    is_coroutine.__graalpython__ = True
    assert fn.__graalpython__
else:
    assert not hasattr(fn, '__graalpython__')
