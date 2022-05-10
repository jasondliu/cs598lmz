fn = lambda: None
# Test fn.__code__.co_filename
fn.__code__.co_filename = 'foo'
# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno = 42
# Test fn.__code__.co_lnotab
fn.__code__.co_lnotab = 'foo'
# Test fn.__code__.co_consts
fn.__code__.co_consts = (None,)
# Test fn.__code__.co_names
fn.__code__.co_names = ('foo',)
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = ('foo',)
# Test fn.__code__.co_freevars
fn.__code__.co_freevars = ('foo',)
# Test fn.__code__.co_cellvars
fn.__code__.co_cellvars = ('foo',)
# Test fn.__code__.co_stacksize
fn.__code__.co_stacksize = 42
# Test
