fn = lambda: None
# Test fn.__code__.co_filename
setattr(fn.__code__, 'co_filename', 'test_code_filename')
assert fn.__code__.co_filename == 'test_code_filename'
del fn.__code__.co_filename

# Test fn.__code__.co_firstlineno
setattr(fn.__code__, 'co_firstlineno', 10)
assert fn.__code__.co_firstlineno == 10
del fn.__code__.co_firstlineno

# Test fn.__code__.co_flags
setattr(fn.__code__, 'co_flags', 0)
assert fn.__code__.co_flags == 0
del fn.__code__.co_flags

# Test fn.__code__.co_lnotab
setattr(fn.__code__, 'co_lnotab', b'\x01\x00')
assert fn.__code__.co_lnotab == b'\x01\x00'
del fn.__code__.co_lnotab

# Test fn.
