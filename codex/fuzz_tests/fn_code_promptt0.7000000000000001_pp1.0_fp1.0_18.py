fn = lambda: None
# Test fn.__code__.co_filename
fn.__code__.co_filename = 'boo'
# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno = 1337
# Test fn.__code__.co_name
fn.__code__.co_name = 'foo'
# Test fn.__code__.co_names
fn.__code__.co_names = ['bar', 'baz']
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = ['spam', 'eggs']
# Test fn.__code__.co_argcount
fn.__code__.co_argcount = 1337

# Test fn.__code__.co_flags
fn.__code__.co_flags = 1337

# Test fn.__code__.co_consts
fn.__code__.co_consts = ('x', 'y')

# Test fn.__code__.co_lnotab
fn.__code__.co_lnotab = 'xyz
