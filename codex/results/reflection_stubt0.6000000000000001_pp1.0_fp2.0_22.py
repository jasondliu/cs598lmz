fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__doc__ = 'doc'
assert fn.__code__ is gi.gi_code
assert fn.__name__ == 'fn'
assert fn.__doc__ == 'doc'
assert fn.__code__.co_filename == gi.gi_code.co_filename
assert fn.__code__.co_name == gi.gi_code.co_name
assert fn.__code__.co_firstlineno == gi.gi_code.co_firstlineno
assert fn.__code__.co_lnotab == gi.gi_code.co_lnotab
assert fn.__code__.co_stacksize == gi.gi_code.co_stacksize
assert fn.__code__.co_flags == gi.gi_code.co_flags
assert fn.__code__.co_consts == gi.gi_code.co_consts
assert fn.__code__.co_names == gi.gi_code.co_names
assert fn
