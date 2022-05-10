fn = lambda: None
# Test fn.__code__
test_fn.__code__

# Test fn.__code__.__dict__
test_fn.__code__.__dict__

# Test fn.__code__.__dict__['co_code']
test_fn.__code__.__dict__['co_code']

# Test fn.__code__.co_filename
test_fn.__code__.co_filename

# Test fn.__code__.co_code_object
test_fn.__code__.co_code

# Test fn.__code__.co_code_object().__doc__
print(test_fn.__code__.co_code.__doc__)

# Test fn.__code__.co_code_object().__class__.__doc__
print(test_fn.__code__.co_code.__class__.__doc__)

# Test fn.__code__.co_code_object().__len__
test_fn.__code__.co_code.__len__

# Test fn.__code__.co_code_object().
