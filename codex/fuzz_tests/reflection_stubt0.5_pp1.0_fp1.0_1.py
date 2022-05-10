fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_non_tuple_code
def fn():
    pass
fn.__code__ = 'foo'
fn()

# test_non_string_code_name
def fn():
    pass
fn.__code__.co_name = 42
fn()

# test_non_string_code_filename
def fn():
    pass
fn.__code__.co_filename = 42
fn()

# test_non_int_code_firstlineno
def fn():
    pass
fn.__code__.co_firstlineno = 'foo'
fn()

# test_non_int_code_lnotab
def fn():
    pass
fn.__code__.co_lnotab = 'foo'
fn()

# test_non_tuple_code_consts
def fn():
    pass
fn.__code__.co_consts = 'foo'
fn()

# test_non_tuple_code_names
def fn():
    pass
fn.__code__.co_names = '
