fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_code_with_non_tuple_co_consts
def fn():
    pass
fn.__code__.co_consts = None
fn()

# test_code_with_non_tuple_co_names
def fn():
    pass
fn.__code__.co_names = None
fn()

# test_code_with_non_tuple_co_varnames
def fn():
    pass
fn.__code__.co_varnames = None
fn()

# test_code_with_non_tuple_co_freevars
def fn():
    pass
fn.__code__.co_freevars = None
fn()

# test_code_with_non_tuple_co_cellvars
def fn():
    pass
fn.__code__.co_cellvars = None
fn()

# test_code_with_non_tuple_co_cell2arg
def fn():
    pass
fn.__code__.co_cell2arg = None

