fn = lambda: None
# Test fn.__code__.co_filename
fn.__code__.co_filename = 'C:\\Python36\\lib\\site-packages\\pytest.py'
# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno = 1
# Test fn.__code__.co_name
fn.__code__.co_name = '__init__'
fn.__code__.co_argcount = 0
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = ('args', 'kwargs')
# Test fn.__code__.co_cellvars
fn.__code__.co_cellvars = ('fn',)
# Test fn.__code__.co_freevars
fn.__code__.co_freevars = ()
# Test fn.__code__.co_consts
fn.__code__.co_consts = (None,)
# Test fn.__code__.co_flags
fn.__code__.co_flags = 67
# Test fn.__code__
