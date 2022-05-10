fn = lambda: None
# Test fn.__code__
assert fn.__code__.__class__.__name__ == 'py_code'
# Test fn.__code__.co_argcount
assert fn.__code__.co_argcount == 0
# Test fn.__code__.co_varnames
assert fn.__code__.co_varnames == ('<lambda>', '__class__')
# Test fn.__code__.co_name
assert fn.__code__.co_name == '<lambda>'
# Test fn.__code__.co_firstlineno
assert fn.__code__.co_firstlineno == 1
# Enable module __main__ code to be used
assert __main__
fn = lambda: None
# Test fn.__code__
assert fn.__code__.__class__.__name__ == 'py_code'
# Test fn.__code__.co_argcount
assert fn.__code__.co_argcount == 0
# Test fn.__code__.co_varnames
assert fn.__code__.co_varnames == ('<lambda>',
