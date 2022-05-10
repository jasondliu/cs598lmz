fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = types.CodeType(0, 0, 0, 0, b'', b'', 0, b'', (), (), (), '', '', 0, b'')
fn.__code__.co_varnames = gi.gi_code.co_varnames = ('__module__',)

# gi.gi_frame = fn.__code__.co_varnames = ('__module__',)

# gi.gi_frame = fn.__code__.co_varnames = ('__module__',)

# gi.gi_frame = fn.__code__.co_varnames = ('__module__',)

# gi.gi_frame = fn.__code__.co_varnames = ('__module__',)

# gi.gi_frame = fn.__code__.co_varnames = ('__module__',)

# gi.gi_frame = fn.__code__.co_varnames = ('__module__',)

# gi.gi_frame = fn.
