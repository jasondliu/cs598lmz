fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__code__.co_filename = '<string>'
fn.__code__.co_firstlineno = 1
fn.__code__.co_name = '<module>'
fn.__code__.co_flags = 0
fn.__code__.co_argcount = 0
fn.__code__.co_consts = ()
fn.__code__.co_names = ()
fn.__code__.co_varnames = ()
fn.__code__.co_freevars = ()
fn.__code__.co_cellvars = ()
fn.__code__.co_stacksize = 0
fn.__code__.co_lnotab = b''
fn.__code__.co_cell2arg = None
fn.__code__.co_zombieframe = None
fn.__code__.co_weakreflist = []
fn.__code__.co_extra = ()
fn.__code__.co_kwonlyargcount = 0
fn.__code__.co_posonly
