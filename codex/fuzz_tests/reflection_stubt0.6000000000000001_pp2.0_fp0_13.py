fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
# fn.__code__.__getattribute__('')
fn.__code__.__init__()
fn.__code__.__iter__()
fn.__code__.__new__()
fn.__code__.__reduce__()
fn.__code__.__reduce_ex__()
fn.__code__.__repr__()
fn.__code__.__setattr__('')
fn.__code__.co_argcount
fn.__code__.co_cellvars
fn.__code__.co_code
fn.__code__.co_consts
fn.__code__.co_filename
fn.__code__.co_firstlineno
fn.__code__.co_flags
fn.__code__.co_freevars
fn.__code__.co_kwonlyargcount
fn.__code__.co_lnotab
fn.__code__.co_name
fn.__code__.co_names
fn.__code__.co_nlocals
fn.__code__.co
