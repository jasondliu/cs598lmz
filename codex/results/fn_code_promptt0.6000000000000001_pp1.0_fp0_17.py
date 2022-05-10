fn = lambda: None
# Test fn.__code__.co_code
fn.__code__.co_code
# Test fn.__code__.co_flags
fn.__code__.co_flags
# Test fn.__code__.co_lnotab
fn.__code__.co_lnotab
# Test fn.__code__.co_name
fn.__code__.co_name
# Test fn.__code__.co_names
fn.__code__.co_names
# Test fn.__code__.co_nlocals
fn.__code__.co_nlocals
# Test fn.__code__.co_stacksize
fn.__code__.co_stacksize
# Test fn.__code__.co_varnames
fn.__code__.co_varnames
# Test fn.__code__.replace
fn.__code__.replace(co_name='foo')
# Test fn.__code__.replace with keyword arguments
fn.__code__.replace(co_name='foo', co_nlocals=1)
# Test fn.__code__.replace
