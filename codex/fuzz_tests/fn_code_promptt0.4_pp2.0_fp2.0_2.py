fn = lambda: None
# Test fn.__code__.co_flags & CO_NOFREE
fn.__code__.co_flags |= CO_NOFREE
assert fn.__code__.co_flags & CO_NOFREE
assert fn.__code__.co_flags & CO_NOFREE == CO_NOFREE
assert fn.__code__.co_flags & CO_NOFREE != 0
assert fn.__code__.co_flags & CO_NOFREE != CO_OPTIMIZED
# Test fn.__code__.co_flags & CO_OPTIMIZED
fn.__code__.co_flags |= CO_OPTIMIZED
assert fn.__code__.co_flags & CO_OPTIMIZED
assert fn.__code__.co_flags & CO_OPTIMIZED == CO_OPTIMIZED
assert fn.__code__.co_flags & CO_OPTIMIZED != 0
assert fn.__code__.co_flags & CO_OPTIMIZED != CO_NOFREE
# Test fn.__code__.co_flags & (CO_NOFREE | CO_
