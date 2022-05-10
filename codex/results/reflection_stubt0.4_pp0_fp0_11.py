fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_code_iter
def fn():
    yield
fn.__code__ = fn.__code__.__code__
fn()

# test_code_iter_2
def fn():
    yield
fn.__code__ = fn.__code__.__code__.__code__
fn()

# test_code_iter_3
def fn():
    yield
fn.__code__ = fn.__code__.__code__.__code__.__code__
fn()

# test_code_iter_4
def fn():
    yield
fn.__code__ = fn.__code__.__code__.__code__.__code__.__code__
fn()

# test_code_iter_5
def fn():
    yield
fn.__code__ = fn.__code__.__code__.__code__.__code__.__code__.__code__
fn()

# test_code_iter_6
def fn():
    yield
fn.__code__ = fn.__code__.__code
