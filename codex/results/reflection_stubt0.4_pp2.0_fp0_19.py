fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_invalid_code_object_co_flags
fn = lambda: None
gi = (i for i in ())
fn.__code__.co_flags = gi
fn()

# test_invalid_code_object_co_code
fn = lambda: None
gi = (i for i in ())
fn.__code__.co_code = gi
fn()

# test_invalid_code_object_co_consts
fn = lambda: None
gi = (i for i in ())
fn.__code__.co_consts = gi
fn()

# test_invalid_code_object_co_names
fn = lambda: None
gi = (i for i in ())
fn.__code__.co_names = gi
fn()

# test_invalid_code_object_co_varnames
fn = lambda: None
gi = (i for i in ())
fn.__code__.co_varnames = gi
fn()

# test_invalid_code_object_co_
