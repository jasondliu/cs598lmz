fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__closure__ = gi.gi_frame.f_code.co_freevars

def __closure__(x):
    return x

def arg(x):
    return x

def foo(a, b):
    return a, b

def bar(**kw):
    return kw

bar(**__closure__(fn.__closure__))    # illegal, will fail
bar(**__closure__(arg(fn.__closure__)))  # this is fine
