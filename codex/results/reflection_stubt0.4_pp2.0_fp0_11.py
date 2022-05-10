fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_code_with_non_tuple_co_consts
fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_code_with_non_tuple_co_names
fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_code_with_non_str_co_name
fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_code_with_non_tuple_co_varnames
fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_code_with_non_int_co_argcount
fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_code_with_negative_co_argcount
fn = lambda: None
gi = (i for i
