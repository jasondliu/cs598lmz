fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = ('a', 'b', 'c')
assert fn.__code__.co_varnames == ('a', 'b', 'c')

fn = lambda: None
# Test fn.__code__.co_argcount
fn.__code__.co_argcount = 1
assert fn.__code__.co_argcount == 1

fn = lambda: None
# Test fn.__code__.co_kwonlyargcount
fn.__code__.co_kwonlyargcount = 1
assert fn.__code__.co_kwonlyargcount == 1

fn = lambda: None
# Test fn.__code__.co_nlocals
fn.__code__.co_nlocals = 1
assert fn.__code__.co_nlocals == 1

fn = lambda: None
# Test fn.__code__.co_stacksize
fn.__code__.co_stacksize = 1
assert fn.__code__.co_stacksize == 1

fn =
