fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = ('a', 'b', 'c')
assert fn.__code__.co_varnames == ('a', 'b', 'c')

# Test fn.__code__.co_argcount
fn.__code__.co_argcount = 1
assert fn.__code__.co_argcount == 1

# Test fn.__code__.co_stacksize
fn.__code__.co_stacksize = 2
assert fn.__code__.co_stacksize == 2

# Test fn.__code__.co_flags
fn.__code__.co_flags = 3
assert fn.__code__.co_flags == 3

# Test fn.__code__.co_code
fn.__code__.co_code = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09'
assert fn.__code__.co_code == b'\x00\x01\x02\
