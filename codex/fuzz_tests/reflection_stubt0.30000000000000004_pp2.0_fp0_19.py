fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_code_object_with_non_code_object_co_code
def fn():
    pass
fn.__code__.co_code = fn
fn()

# test_code_object_with_non_tuple_co_consts
def fn():
    pass
fn.__code__.co_consts = None
fn()

# test_code_object_with_non_tuple_co_names
def fn():
    pass
fn.__code__.co_names = None
fn()

# test_code_object_with_non_tuple_co_varnames
def fn():
    pass
fn.__code__.co_varnames = None
fn()

# test_code_object_with_non_tuple_co_freevars
def fn():
    pass
fn.__code__.co_freevars = None
fn()

# test_code_object_with_non_tuple_co_cellvars
def fn():
    pass
fn.__code__
