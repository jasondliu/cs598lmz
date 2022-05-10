fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = type(gi.gi_code)()
fn.__code__.co_filename = gi.gi_code.co_filename = '<foo>'
fn.__code__.co_firstlineno = gi.gi_code.co_firstlineno = 42
fn.__code__.co_name = gi.gi_code.co_name = 'foo'
fn.__code__.co_varnames = gi.gi_code.co_varnames = ('a', 'b')
fn.__code__.co_argcount = gi.gi_code.co_argcount = 2
fn.__code__.co_flags = gi.gi_code.co_flags = 0
fn.__code__.co_freevars = gi.gi_code.co_freevars = ()
fn.__code__.co_cellvars = gi.gi_code.co_cellvars = ()
fn.__code__.co_stacksize = gi.gi_code.co_stacksize =
