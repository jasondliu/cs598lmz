fn = lambda: None
# Test fn.__code__
fn2.__code__
# Test fn.__code__.co_consts
fn.__code__.co_consts == fn2.__code__.co_consts

# Test fn.__code__.co_filename
fn2.__code__.co_filename
# Test fn.__code__.co_lnotab
fn.__code__.co_lnotab == fn2.__code__.co_lnotab
# Test fn.__code__.co_name
fn2.__code__.co_name
# Test fn.__code__.co_names
fn.__code__.co_names == fn2.__code__.co_names

# Test fn.__code__.co_nlocals
fn2.__code__.co_nlocals
# Test fn.__code__.co_stacksize
fn.__code__.co_stacksize == fn2.__code__.co_stacksize
# Test fn.__code__.co_varnames
fn.__code__.co_varnames
