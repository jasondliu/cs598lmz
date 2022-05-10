fn = lambda: None
gi = (i for i in ())
fn.__code__ = fn.__code__.__new__(fn.__code__.__class__)
fn.__code__.co_consts = (None, None, None, None)
fn.__code__.co_lnotab = ''
fn.__code__.co_freevars = ()
fn.__code__.co_cellvars = ()
fn.__code__.co_stacksize = 1
