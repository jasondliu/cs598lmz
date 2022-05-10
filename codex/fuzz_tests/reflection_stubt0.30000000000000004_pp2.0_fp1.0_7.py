fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_code_with_non_code_co_consts
fn = lambda: None
fn.__code__ = (i for i in ())
fn()

# test_code_with_non_tuple_co_consts
fn = lambda: None
fn.__code__ = [None]
fn()

# test_code_with_non_str_co_consts
fn = lambda: None
fn.__code__ = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None
