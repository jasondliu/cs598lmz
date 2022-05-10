fn = lambda: None
# Test fn.__code__.co_flags & 0x4 == 0
# test False

# Test fn = lambda x: x
# Test fn.__code__.co_flags & 0x4 == 0
# test False

# Test fn = lambda x=1: x
# Test fn.__code__.co_flags & 0x4 == 0
# test False

# Test fn = lambda x, y, z=1: x+y+z
# Test fn.__code__.co_flags & 0x4 == 0
# test False

# Test fn = lambda *args: args
# Test fn.__code__.co_flags & 0x4 == 0
# test False

# Test fn = lambda **kargs: kargs
# Test fn.__code__.co_flags & 0x4 == 0
# test False

# Test fn = lambda x, *args, **kargs: x+args+kargs
# Test fn.__code__.co_flags & 0x4 == 0
# test False

# Test fn = lambda *args, **kargs: args+kargs
# Test
