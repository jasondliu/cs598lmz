fn = lambda: None
gi = (i for i in ())
fn.__code__ = fn.__code__.replace(co_freevars, b'()')
fn.__name__ = '_'
fn.__closure__ = (gi,)
del fn
