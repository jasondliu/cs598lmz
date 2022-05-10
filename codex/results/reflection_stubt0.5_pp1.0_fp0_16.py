fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# test_code_with_bad_co_flags
def fn():
    pass
fn.__code__.co_flags = 10
fn()

# test_code_with_bad_co_lnotab
def fn():
    pass
fn.__code__.co_lnotab = b'\x00'
fn()

# test_code_with_bad_co_nlocals
def fn():
    pass
fn.__code__.co_nlocals = -1
fn()

# test_code_with_bad_co_name
def fn():
    pass
fn.__code__.co_name = 'a'
fn()

# test_code_with_bad_co_names
def fn():
    pass
fn.__code__.co_names = (1,)
fn()

# test_code_with_bad_co_varnames
def fn():
    pass
fn.__code__.co_varnames = (1,)
fn()

# test_code
