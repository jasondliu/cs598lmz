fn = lambda: None
# Test fn.__code__.co_filename's value is __file__
fn.__code__.co_filename = __file__
# Test fn.__code__.co_name's value is 'fn'
fn.__code__.co_name = 'fn'
# Test fn.__code__.co_firstlineno's value is 14
fn.__code__.co_firstlineno = 14
test_fn = fn
test_fn()
# Test fn.__code__.co_varnames's value is ('test_fn',)
test_fn = fn
test_fn()

# Test fn.__code__.co_argcount's value is 0
fn = lambda: None
# Test fn.__code__.co_argcount's value is 1
fn = lambda arg0: None
# Test fn.__code__.co_argcount's value is 2
fn = lambda arg0, arg1: None
# Test fn.__code__.co_argcount's value is 3
fn = lambda arg0, arg1, arg2: None
# Test fn.__code__.co_argcount's
