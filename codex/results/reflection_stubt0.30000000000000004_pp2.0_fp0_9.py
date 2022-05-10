fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_code_co_flags
def fn():
    pass
fn.__code__.co_flags = 0

# test_code_co_freevars
def fn():
    pass
fn.__code__.co_freevars = ()

# test_code_co_names
def fn():
    pass
fn.__code__.co_names = ()

# test_code_co_varnames
def fn():
    pass
fn.__code__.co_varnames = ()

# test_code_co_cellvars
def fn():
    pass
fn.__code__.co_cellvars = ()

# test_code_co_consts
def fn():
    pass
fn.__code__.co_consts = ()

# test_code_co_filename
def fn():
    pass
fn.__code__.co_filename = ''

# test_code_co_firstlineno
def fn():
    pass
fn.__code__.co_firstlineno = 0
