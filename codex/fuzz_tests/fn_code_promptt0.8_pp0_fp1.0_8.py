fn = lambda: None
# Test fn.__code__.co_flags
setattr(fn, "__code__", code)
try:
    fn.__code__.co_flags
except AttributeError:
    pass
else:
    raise RuntimeError("test failed")

code = types.CodeType
# Test code.__code__.co_flags
try:
    code.__code__.co_flags
except AttributeError:
    pass
else:
    raise RuntimeError("test failed")
