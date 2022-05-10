fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_code_co_flags
def f():
    pass
f.__code__.co_flags

# test_code_co_lnotab
def f():
    pass
f.__code__.co_lnotab

# test_code_co_name
def f():
    pass
f.__code__.co_name

# test_code_co_names
def f():
    pass
f.__code__.co_names

# test_code_co_nlocals
def f():
    pass
f.__code__.co_nlocals

# test_code_co_stacksize
def f():
    pass
f.__code__.co_stacksize

# test_code_co_varnames
def f():
    pass
f.__code__.co_varnames

# test_code_co_argcount
def f():
    pass
f.__code__.co_argcount

# test_code_co_consts
def f():

