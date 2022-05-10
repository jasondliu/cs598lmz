fn = lambda: None
# Test fn.__code__
test_fn.__code__
test_fn.__code__.co_argcount
test_fn.__code__.co_name
test_fn.__code__.co_filename

# Test fn.__globals__
test_fn = lambda x: x
test_fn.__globals__
test_fn.__globals__['__name__']
test_fn.__globals__['test_fn']
