fn = lambda: None
# Test fn.__code__.co_freevars
fn.__code__.co_freevars = ('a',)
# Test fn.__code__.co_cellvars
fn.__code__.co_cellvars = ('b',)
# Test fn.__code__.co_filename
fn.__code__.co_filename = 'a.py'
# Test fn.__code__.co_name
fn.__code__.co_name = 'fn'

# Test fn.__code__.co_argcount
fn.__code__.co_argcount = 2
# Test fn.__code__.co_kwonlyargcount
fn.__code__.co_kwonlyargcount = 1
# Test fn.__code__.co_nlocals
fn.__code__.co_nlocals = 3
# Test fn.__code__.co_stacksize
fn.__code__.co_stacksize = 10
# Test fn.__code__.co_flags
fn.__code__.co_flags = 0
# Test fn.__code__.co
