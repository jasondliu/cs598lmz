fn = lambda: None
# Test fn.__code__.co_filename
test_fn.__code__.co_filename

# Test custom files
test = os.path.join('test', 'test_fn.py')
test_fn = parse_function(test, 'test_fn')
test_fn.__code__.co_filename

# Test absolute path parsing
path = os.path.abspath(test)
test_fn = parse_function(path, 'test_fn')
test_fn.__code__.co_filename == path
