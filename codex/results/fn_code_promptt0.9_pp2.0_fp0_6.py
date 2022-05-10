fn = lambda: None
# Test fn.__code__ to avoid crashes if fn is a bound method
if hasattr(fn, '__code__'):
    fn.__code__.co_flags &= ~CO_HAS_FREE_VARS
</code>

