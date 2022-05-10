fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
try:
    fn()
except TypeError as e:
    assert str(e) == 'code object passed to builtin_function_or_method() ' \
                     'has no __code__ attribute'
else:
    assert False

# This should not raise a SystemError
fn.__code__ = None
fn()

# This should not raise a SystemError
fn.__code__ = 42
fn()
