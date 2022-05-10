fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = ('a', 'b')
# Test fn.__code__.co_argcount
fn.__code__.co_argcount = 2
# Test fn.__code__.co_posonlyargcount
fn.__code__.co_posonlyargcount = 2
# Test fn.__code__.co_kwonlyargcount
fn.__code__.co_kwonlyargcount = 2
# Test fn.__code__.co_stacksize
fn.__code__.co_stacksize = 2
# Test fn.__code__.co_flags
fn.__code__.co_flags = 2
# Test fn.__code__.co_consts
fn.__code__.co_consts = (1, 2)
# Test fn.__code__.co_names
fn.__code__.co_names = ('a', 'b')
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = ('a', 'b')
