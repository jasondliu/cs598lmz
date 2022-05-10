fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_code_with_non_tuple_co_consts
def fn():
    pass
fn.__code__.co_consts = 1
fn()

# test_code_with_non_tuple_co_names
def fn():
    pass
fn.__code__.co_names = 1
fn()

# test_code_with_non_tuple_co_varnames
def fn():
    pass
fn.__code__.co_varnames = 1
fn()

# test_code_with_non_tuple_co_freevars
def fn():
    pass
fn.__code__.co_freevars = 1
fn()

# test_code_with_non_tuple_co_cellvars
def fn():
    pass
fn.__code__.co_cellvars = 1
fn()

# test_code_with_non_tuple_co_cell2arg
def fn():
    pass
fn.__code__.co_cell2arg = 1

