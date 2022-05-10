fn = lambda: None
# Test fn.__code__.co_filename
fn.__code__.co_filename = "x"
fn()
# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno = 1
fn()
# Test fn.__code__.co_argcount
fn.__code__.co_argcount = 1
fn()
# Test fn.__code__.co_kwonlyargcount
fn.__code__.co_kwonlyargcount = 1
fn()
# Test fn.__code__.co_nlocals
fn.__code__.co_nlocals = 1
fn()
# Test fn.__code__.co_stacksize
fn.__code__.co_stacksize = 1
fn()
# Test fn.__code__.co_flags
fn.__code__.co_flags = 1
fn()
# Test fn.__code__.co_code
fn.__code__.co_code = bytes([1, 2, 3])
fn()
# Test fn.__code__.co_consts
fn.__code
