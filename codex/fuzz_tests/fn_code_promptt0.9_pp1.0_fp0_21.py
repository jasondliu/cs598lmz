fn = lambda: None
# Test fn.__code__.co_firstlineno
test_fn.__code__.co_firstlineno

# Test fn.__code__.co_lnotab
test_fn.__code__.co_lnotab

def fn_with_docstring(a, b, c=10, *args, **kwargs):
    '''A test docstring.'''
    return a + b + c
# Test fn_with_docstring.__doc__
fn_with_docstring.__doc__

# Test fn_with_docstring.__code__.co_firstlineno
fn_with_docstring.__code__.co_firstlineno

# Test fn_with_docstring.__code__.co_lnotab
fn_with_docstring.__code__.co_lnotab

# Test fn_with_docstring.__code__.co_consts
fn_with_docstring.__code__.co_consts

# Another object
value = 10
# Test value.__class__
value.__class__

# Test value.__
