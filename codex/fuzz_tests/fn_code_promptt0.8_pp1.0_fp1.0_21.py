fn = lambda: None
# Test fn.__code__.co_firstlineno attribute
test_fn.__code__.co_firstlineno == 2
'''


def test_lambda_code_object():
    '''
    Test that lambda expressions have code objects (like normal functions)
    '''
    test_lambda = lambda x: x
    assert hasattr(test_lambda, '__code__')


def test_has_closure():
    '''
    Test that lambda expressions have a __closure__ attribute
    '''
    closure_var = 'test'
    test_lambda = lambda x: x + closure_var
    assert hasattr(test_lambda, '__closure__')


def test_closure_contents():
    '''
    Test that __closure__ returns the vars referenced in the lambda
    '''
    closure_var = 'test'
    test_lambda = lambda x: x + closure_var
    # Verify length of tuple is one, since there is only one var used within
    # the function
    assert len(test_lambda.__closure__) == 1
    # Verify that the contents of the closure
