fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = type(gi.gi_code)()
fn.__code__.co_varnames = ('a', 'b', 'c')
fn.__code__.co_argcount = 3
fn.__code__.co_flags = 67
fn.__code__.co_code = b'|\x00\x00S\x00'
fn.__code__.co_consts = (None, 'a', 'b', 'c')
fn.__code__.co_names = ('namedtuple', 'Point')
fn.__code__.co_lnotab = b'\x00\x01\x0c\x01\x08\x01'
fn.__code__.co_stacksize = 2
fn.__code__.co_firstlineno = 1
fn.__code__.co_name = '<lambda>'
fn.__code__.co_filename = '<stdin>'
fn.__code__.co_freevars = ()
fn.__code__.co_cellvars = ()
