fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_code_object_with_non_tuple_co_consts
fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_code_object_with_non_tuple_co_freevars
fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_code_object_with_non_tuple_co_varnames
fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_code_object_with_non_tuple_co_cellvars
fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_code_object_with_non_tuple_co_names
fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_code_object_with_non_
