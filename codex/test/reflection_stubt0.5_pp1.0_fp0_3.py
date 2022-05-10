fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_frame.f_code
fn.__name__ = 'fn'

# The following line should not throw an AttributeError
fn.__code__.co_filename

# The following line should not throw an AttributeError
fn.__code__.co_firstlineno

# The following line should not throw an AttributeError
fn.__code__.co_name

# The following line should not throw an AttributeError
fn.__code__.co_argcount

# The following line should not throw an AttributeError
fn.__code__.co_flags

# The following line should not throw an AttributeError
fn.__code__.co_varnames

# The following line should not throw an AttributeError
fn.__code__.co_consts

# The following line should not throw an AttributeError
fn.__code__.co_names

# The following line should not throw an AttributeError
fn.__code__.co_nlocals

# The following line should not throw an AttributeError
