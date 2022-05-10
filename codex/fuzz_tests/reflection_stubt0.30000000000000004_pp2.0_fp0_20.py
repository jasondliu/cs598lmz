fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_code_is_not_callable
def fn():
    pass
fn.__code__ = 1
fn()

# test_code_is_not_code
def fn():
    pass
fn.__code__ = 1
fn()

# test_code_is_not_tuple
def fn():
    pass
fn.__code__ = 1
fn()

# test_code_is_not_tuple2
def fn():
    pass
fn.__code__ = 1
fn()

# test_code_is_not_tuple3
def fn():
    pass
fn.__code__ = 1
fn()

# test_code_is_not_tuple4
def fn():
    pass
fn.__code__ = 1
fn()

# test_code_is_not_tuple5
def fn():
    pass
fn.__code__ = 1
fn()

# test_code_is_not_tuple6
def fn():
    pass
fn.__code__ = 1

