fn = lambda: None
# Test fn.__code__.co_varnames against fn.__code__.co_argcount
def test_fn_argcount():
    assert test_fn.__code__.co_argcount == len(test_fn.__code__.co_varnames)
# Test fn_argcount() against fn_args()
def test_fn_argcount_against_fn_args():
    assert fn_argcount(test_fn) == len(fn_args(test_fn))

# Test fn_varnames()
def test_fn_varnames():
    assert fn_varnames(test_fn) == test_fn.__code__.co_varnames


# Test fn_defaults()
def test_fn_defaults():
    assert fn_defaults(test_fn) == test_fn.__defaults__
# Test fn_defaults() against fn_args()
def test_fn_defaults_against_fn_args():
    assert len(test_fn.__code__.co_varnames) - test_fn.__code__.co_argcount
