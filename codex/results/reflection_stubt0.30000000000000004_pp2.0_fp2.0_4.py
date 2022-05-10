fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_code_with_non_function_closure
fn = lambda: None
fn.__code__ = lambda: None
fn()

# test_code_with_non_tuple_closure
fn = lambda: None
fn.__code__ = (lambda: None,)
fn()

# test_code_with_non_tuple_freevars
fn = lambda: None
fn.__code__ = (lambda: None, (), None)
fn()

# test_code_with_non_tuple_cellvars
fn = lambda: None
fn.__code__ = (lambda: None, (), (), ())
fn()

# test_code_with_non_tuple_varnames
fn = lambda: None
fn.__code__ = (lambda: None, (), (), (), ())
fn()

# test_code_with_non_string_name
fn = lambda: None
fn.__code__ = (lambda: None, (), (), (), (), ())
fn()

# test_code_with_non_string_filename
fn =
