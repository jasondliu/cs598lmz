import types
types.MethodType(lambda x: x, None)
sys.gettrace()

# Issue #16335: Test that the C implementation of the lru_cache decorator
# correctly handles function attributes.

@functools.lru_cache(maxsize=2)
def f():
    "Doc"
    pass

# Attributes set before the decorator should still be there after.
f.foo = 'bar'
assert f.foo == 'bar'
assert f.__doc__ == "Doc"
assert f.__name__ == "f"
assert f.__module__ == __name__

# Attributes set after the decorator should also be there after.
f.bar = 'baz'
assert f.foo == 'bar'
assert f.bar == 'baz'

# Verify attributes are reset after the cache is cleared.
f.clear()
assert not hasattr(f, 'foo')
assert not hasattr(f, 'bar')

# Issue #16371: Test that the C implementation of the lru_cache decorator
# clears the cache when the underlying function is deleted.

