fn = lambda: None
# Test fn.__code__
fn.__code__ = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# Test fn.__code__.co_filename
fn.__code__.co_filename = 'test'
# Test fn.__code__.co_name
fn.__code__.co_name = 'test'
# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno = 0
# Test fn.__closure__
fn.__closure__ = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# Test fn.__closure__[0].cell_contents
fn.__closure__[0].cell_contents = 11
# Test fn.__closure__[0]
fn.__closure__[0] = 11
# Test fn.__globals__
fn.__globals__ = {1:2}
# Test fn.__globals__[1]
fn.__globals__[1] = 1
# Test fn.__defaults__
