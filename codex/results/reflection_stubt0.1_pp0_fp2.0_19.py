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

# test_code_co_stacksize
def f():
    pass
f.__code__.co_stacksize = 0

# test_code_co_varnames
def f():
    pass
f.__code__.co_varnames = ()

# test_code_co_filename
def f():
    pass
f.__code__.co_filename = ''

# test_code_co_name
def f():
    pass
f.__code__.co_name = ''

# test_code_co_firstlineno
def f():
    pass
f.__code__.co_firstlineno = 0

