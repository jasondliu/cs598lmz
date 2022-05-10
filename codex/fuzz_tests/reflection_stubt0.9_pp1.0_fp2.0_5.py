fn = lambda: None
gi = (i for i in ())
fn.__code__ = fn.func_code = fi
fn.__closure__ = fn.func_closure = (gi, )
