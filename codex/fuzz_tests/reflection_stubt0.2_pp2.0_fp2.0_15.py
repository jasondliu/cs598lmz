fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_code_new_empty_code
def fn():
    pass
fn.__code__ = type(fn.__code__)(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'')
fn()

# test_code_new_from_code
def fn():
    pass
fn.__code__ = type(fn.__code__).from_code(fn.__code__)
fn()

# test_code_new_kwonlyargcount
def fn():
    pass
fn.__code__ = type(fn.__code__)(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'', 0)
fn()

# test_code_new_kwonlyargcount_negative
def fn():
    pass
fn.__code__ = type(fn.__code__)(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'', -1)
fn()

# test_code_new_kwonlyargcount_
