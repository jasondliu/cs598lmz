fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_code_co_flags
def f():
    pass
f.__code__.co_flags = 0

# test_code_co_lnotab
def f():
    pass
f.__code__.co_lnotab = b''

# test_code_co_names
def f():
    pass
f.__code__.co_names = ()

# test_code_co_varnames
def f():
    pass
f.__code__.co_varnames = ()

# test_code_co_cellvars
def f():
    pass
f.__code__.co_cellvars = ()

# test_code_co_freevars
def f():
    pass
f.__code__.co_freevars = ()

# test_code_co_consts
def f():
    pass
f.__code__.co_consts = ()

# test_code_co_stacksize
def f():
    pass
f.__code__.co_
