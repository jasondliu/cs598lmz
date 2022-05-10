fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = type(gi.gi_frame.f_code)()
fn.__code__.co_varnames = ('a', 'b')
fn.__code__.co_argcount = 2
fn.__code__.co_flags = 0x4
fn.__code__.co_nlocals = 2
fn.__code__.co_stacksize = 2
fn.__code__.co_filename = '<stdin>'
fn.__code__.co_firstlineno = 1
fn.__code__.co_lnotab = b''
fn.__code__.co_freevars = ()
fn.__code__.co_cellvars = ()
fn.__code__.co_consts = (None,)
fn.__code__.co_names = ()
fn.__code__.co_varnames = ('a', 'b')
fn.__code__.co_argcount = 2
fn.__code__.co_posonlyargcount = 0
fn.__code__.co_kwonlyargcount
