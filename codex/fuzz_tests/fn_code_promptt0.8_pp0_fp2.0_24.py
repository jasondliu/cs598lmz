fn = lambda: None
# Test fn.__code__.co_filename
fn.__code__.co_filename = '<stdin>'
# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno = 1
# Test fn.__code__.co_lnotab
fn.__code__.co_lnotab = [1, 2, 3]
# Test fn.__code__.co_name
fn.__code__.co_name = 'test'
# Test fn.__code__.co_names
fn.__code__.co_names = []
# Test fn.__code__.co_nlocals
fn.__code__.co_nlocals = 1
# Test fn.__code__.co_stacksize
fn.__code__.co_stacksize = 1
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = []

# Test fn.__code__.co_consts
fn.__code__.co_consts == (None, 1, 1.1, "foo")
