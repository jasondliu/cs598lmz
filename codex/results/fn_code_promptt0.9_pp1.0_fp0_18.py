fn = lambda: None
# Test fn.__code__ is set.
test_fn.__code__ = 0
# Test fn.__closure__ is set.
test_fn.__closure__ = 0
# Test fn.__func__ is set.
test_fn.__func__ = 0
# Test fn.__get__ is set.
test_fn.__get__ = 0
# Test fn.__globals__ is set.
test_fn.__globals__ = 0
# Test fn.__name__ is set.
test_fn.__name__ = 0
# Test fn.__repr__ is set.
test_fn.__repr__ = 0
# Test fn.__self__ is set.
test_fn.__self__ = 0
# Test fn.__text_signature__ is set.
test_fn.__text_signature__ = 0
# Test fn.__weakref__ is set.
test_fn.__weakref__ = 0
# Test fn.pyx.0 is set.
test_fn.pyx.0 = 0
test_fn(a=0)
test_fn(b=
