fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__code__.co_filename = co_filename
fn.__code__.co_firstlineno = co_firstlineno
fn.__code__.co_lnotab = co_lnotab
fn.__code__.co_stacksize = co_stacksize
fn.__code__.co_flags = co_flags
fn.__code__.co_consts = co_consts
fn.__code__.co_names = co_names
fn.__code__.co_varnames = co_varnames
fn.__code__.co_freevars = co_freevars
fn.__code__.co_cellvars = co_cellvars
fn.__code__.co_nlocals = co_nlocals
fn.__code__.co_argcount = co_argcount
fn.__code__.co_kwonlyargcount = co_kwonlyargcount
fn.__code__.co_posonlyargcount = co_posonlyargcount
fn.__code__.co_
