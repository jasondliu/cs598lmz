fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
gi.gi_frame = fn
gi.gi_code = fn
gi.gi_frame.f_lineno = 1

def func():
    pass

def func():
    pass

def func(*, garbage=1):
    pass

def func(**garbage):
    pass

def func(*args, garbage=1):
    pass

def func(*args, **kwargs):
    pass

def func(*args, **kwargs):
    pass

def func(*, garbage=1, **kwargs):
    pass

def func(arg, *args, **kwargs):
    pass

def func(arg, *args, garbage=1, **kwargs):
    pass

def func(arg, a=1, *args, *, k=1, **kwargs):
    pass

def func(arg, *, k=1, **kwargs):
    pass

def func(arg, *, k=1):
    pass

def func(arg):
    pass

def func(arg=1):
    pass

