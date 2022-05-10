fn = lambda: None
# Test fn.__code__.co_argcount
fn.__code__.co_argcount = 0
fn.__code__.co_argcount = 1
fn.__code__.co_argcount = 2
# Test fn.__code__.co_cellvars
fn.__code__.co_cellvars = ()
fn.__code__.co_cellvars = ('a',)
fn.__code__.co_cellvars = ('a', 'b')
# Test fn.__code__.co_code
fn.__code__.co_code = b''
fn.__code__.co_code = b'\x00\x00'
fn.__code__.co_code = b'\x00\x00\x00\x00'
# Test fn.__code__.co_consts
fn.__code__.co_consts = ()
fn.__code__.co_consts = (None,)
fn.__code__.co_consts = (None, 1)
# Test fn.__code__.co_filename
fn.__code__
