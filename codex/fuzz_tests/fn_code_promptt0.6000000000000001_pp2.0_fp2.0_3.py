fn = lambda: None
# Test fn.__code__
TestFn.test_fn.__code__
# Test fn.__closure__
TestFn.test_fn.__closure__
# Test fn.__defaults__
TestFn.test_fn.__defaults__
# Test fn.__get__
TestFn.test_fn.__get__(TestFn, type(TestFn))
# Test fn.__globals__
TestFn.test_fn.__globals__
# Test fn.__kwdefaults__
TestFn.test_fn.__kwdefaults__
# Test fn.__name__
TestFn.test_fn.__name__
# Test fn.__qualname__
TestFn.test_fn.__qualname__

# Test fn.__call__
TestFn.test_fn(TestFn)
# Test fn.__delattr__
delattr(TestFn.test_fn, '__code__')
# Test fn.__dir__
dir(TestFn.test_fn)
# Test fn.__eq__
TestFn.
