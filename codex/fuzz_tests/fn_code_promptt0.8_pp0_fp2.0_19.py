fn = lambda: None
# Test fn.__code__.co_varnames
test_fn.__code__ = mock_code
assert test_fn.__code__.co_varnames == ('a', 'b', 'c')

# Test mock_code.co_varnames
assert mock_code.co_varnames == ('a', 'b', 'c')

# Test mock_code.co_varnames 
