fn = lambda: None
# Test fn.__code__.co_filename
fn.__code__.co_filename = 'foo'
fn.__code__.co_filename = ''
fn.__code__.co_filename = 'bar'

# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno = 0
fn.__code__.co_firstlineno = 100
fn.__code__.co_firstlineno = 200

# Test fn.__code__.co_flags
fn.__code__.co_flags = 0
fn.__code__.co_flags = 1
fn.__code__.co_flags = 2

# Test fn.__code__.co_freevars
fn.__code__.co_freevars = ()
fn.__code__.co_freevars = ('a', 'b')
fn.__code__.co_freevars = ('c', 'd')

# Test fn.__code__.co_kwonlyargcount
fn.__code__.co_kwonlyargcount = 0
fn.__code__.
