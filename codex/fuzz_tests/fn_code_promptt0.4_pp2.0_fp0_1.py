fn = lambda: None
# Test fn.__code__.co_filename
setattr(fn, "__code__", lambda: None)
setattr(fn.__code__, "co_filename", "test")
assert fn.__code__.co_filename == "test"
# Test fn.__code__.co_firstlineno
setattr(fn, "__code__", lambda: None)
setattr(fn.__code__, "co_firstlineno", 1)
assert fn.__code__.co_firstlineno == 1
# Test fn.__code__.co_flags
setattr(fn, "__code__", lambda: None)
setattr(fn.__code__, "co_flags", 1)
assert fn.__code__.co_flags == 1
# Test fn.__code__.co_lnotab
setattr(fn, "__code__", lambda: None)
setattr(fn.__code__, "co_lnotab", "test")
assert fn.__code__.co_lnotab == "test"
# Test fn.__code__.co_name
setattr(fn
