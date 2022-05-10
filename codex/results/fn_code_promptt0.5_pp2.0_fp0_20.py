fn = lambda: None
# Test fn.__code__
fn.__code__ = code
# Test fn.__code__.co_filename
fn.__code__.co_filename = 'filename'
# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno = 10
# Test fn.__code__.co_name
fn.__code__.co_name = 'test'

# Test fn.__defaults__
fn.__defaults__ = None
# Test fn.__defaults__
fn.__defaults__ = (1, 2, 3)
# Test fn.__defaults__
fn.__defaults__ = (1, 2)
# Test fn.__defaults__
fn.__defaults__ = (1,)
# Test fn.__defaults__
fn.__defaults__ = (1, 2, 3, 4, 5, 6, 7)
# Test fn.__defaults__
fn.__defaults__ = (1, 2, 3, 4, 5, 6, 7, 8)
# Test fn.__defaults__
fn.__defaults__
