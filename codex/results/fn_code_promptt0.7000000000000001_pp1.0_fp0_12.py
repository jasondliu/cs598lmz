fn = lambda: None
# Test fn.__code__
test_fn.__code__
# Test fn.__code__.__args__
test_fn.__code__.__args__
# Test fn.__code__.__defaults__
test_fn.__code__.__defaults__
# Test fn.__code__.__kwdefaults__
test_fn.__code__.__kwdefaults__
# Test fn.__annotations__
test_fn.__annotations__
# Test fn.__code__.__annotations__
test_fn.__code__.__annotations__

class TestClass:
    pass

# Test TestClass.__dict__
TestClass.__dict__
# Test TestClass.__dict__['__module__']
TestClass.__dict__['__module__']
# Test TestClass.__module__
TestClass.__module__
# Test TestClass.__doc__
TestClass.__doc__
