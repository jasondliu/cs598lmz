fn = lambda: None
# Test fn.__code__.co_argcount
fn.__code__.co_argcount = 2
# Test fn.__code__.co_nlocals
fn.__code__.co_nlocals = 2
# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno = 2

# Test fn.__code__.co_lnotab
co_lnotab = b'\x01\x00\x01\x00'
fn.__code__.co_lnotab = co_lnotab

# Test fn.__code__.co_code
co_code = b'\x01\x00\x02\x00'
fn.__code__.co_code = co_code

# Test fn.__code__.co_consts
co_consts = (None, 2, 'test')
fn.__code__.co_consts = co_consts

# Test fn.__code__.co_names
co_names = ('None', '2', 'test', 'fn')
fn.__code
