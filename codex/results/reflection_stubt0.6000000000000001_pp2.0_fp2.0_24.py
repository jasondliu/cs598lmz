fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'test'
fn()

# This is ignored if the code object is a generator
fn.__code__ = (lambda: (yield) for i in ()).gi_code
fn.__name__ = 'test'
fn()

# This is ignored if the code object is a generator
fn.__code__ = (lambda: (yield) for i in ()).gi_frame.f_code
fn.__name__ = 'test'
fn()

# This is ignored if the code object is a generator
fn.__code__ = (lambda: (yield) for i in ()).gi_frame.f_back.f_code
fn.__name__ = 'test'
fn()

# This is ignored if the code object is a generator
fn.__code__ = (lambda: (yield) for i in ()).gi_frame.f_back.f_back.f_code
fn.__name__ = 'test'
fn()

# This is ignored if the code object is a generator
fn.__code__ =
