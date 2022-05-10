fn = lambda: None
# Test fn.__code__.co_filename
fn.__code__.co_filename = 'foo.py'
# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno = 1
# Test fn.__code__.co_lnotab
fn.__code__.co_lnotab = b'\x01\x01'
# Test fn.__code__.co_consts
fn.__code__.co_consts = (None,)
# Test fn.__code__.co_names
fn.__code__.co_names = ('None',)
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = ('fn',)
# Test fn.__code__.co_freevars
fn.__code__.co_freevars = ('fn',)
# Test fn.__code__.co_cellvars
fn.__code__.co_cellvars = ('fn',)
# Test fn.__code__.co_stacksize
fn.__code__.co_
