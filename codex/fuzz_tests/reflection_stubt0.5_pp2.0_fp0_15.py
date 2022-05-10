fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# test codeobj.co_flags
def f(a, b, c=1, d=2, e=3, *g, **h):
    pass

assert f.__code__.co_flags == 67

# test codeobj.co_consts
def f(): pass

assert f.__code__.co_consts == (None,)

# test codeobj.co_names
def f(): pass

assert f.__code__.co_names == ()

# test codeobj.co_varnames
def f(): pass

assert f.__code__.co_varnames == ()

# test codeobj.co_freevars
def f(): pass

assert f.__code__.co_freevars == ()

# test codeobj.co_cellvars
def f(): pass

assert f.__code__.co_cellvars == ()

# test codeobj.co_filename
def f(): pass

assert f.__code__.co_filename == __file__

