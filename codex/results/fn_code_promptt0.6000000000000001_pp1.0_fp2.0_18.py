fn = lambda: None
# Test fn.__code__.co_filename
fn.__code__.co_name = '<lambda>'
# Test fn.__code__.co_firstlineno
fn.__code__.co_lnotab = b'\x02\x01\x01\x01\x01\x01\x01\x01\x02\x01\x01\x01\x02\x01\x01\x01\x02\x01\x01\x01\x02\x01\x01\x01'
fn.__code__.co_nlocals = 1
fn.__code__.co_stacksize = 2
fn.__code__.co_flags = 67
fn.__code__.co_consts = (None, '<code object <lambda> at ', ', file ', ', line ', '>')
fn.__code__.co_names = ()
fn.__code__.co_varnames = ()
fn.__code__.co_freevars = ()
fn.__code__.co_cellvars = ()
# Test fn.__
