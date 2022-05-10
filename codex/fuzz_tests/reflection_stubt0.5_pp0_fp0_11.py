fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = type(gi.gi_code)()
fn.__code__.co_filename = gi.gi_code.co_filename = '<foo>'
fn.__code__.co_firstlineno = gi.gi_code.co_firstlineno = 1
fn.__code__.co_name = gi.gi_code.co_name = '<lambda>'
fn.__code__.co_lnotab = gi.gi_code.co_lnotab = b'\x00\x01'
fn.__code__.co_argcount = gi.gi_code.co_argcount = 0
fn.__code__.co_varnames = gi.gi_code.co_varnames = ()
fn.__code__.co_filename = gi.gi_code.co_filename = '<foo>'
fn.__code__.co_flags = gi.gi_code.co_flags = 0
fn.__code__.co_code = gi.gi_code.co_code
