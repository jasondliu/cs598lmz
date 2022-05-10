fn = lambda: None
# Test fn.__code__.co_argcount == 2
fn.__code__ = MagicMock(co_argcount=2)

# Test fn.__code__.co_argcount == 0
fn.__code__.co_argcount = 0
"""


def test_kwarg_only_args_error(fn):
    with pytest.raises(ValueError):
        fn.__code__.co_argcount = 1
        fn.__code__.co_kwonlyargcount = 1
        kwarg_only_args(fn)


def test_kwarg_only_args(fn):
    fn.__code__.co_argcount = 0
    fn.__code__.co_kwonlyargcount = 1
    kwargs = kwarg_only_args(fn)
    assert len(kwargs) == 1
    assert kwargs[0].name == 'kwarg'


def test_kwarg_only_args_multi(fn):
    fn.__code__.co_argcount = 0
    fn.__code__.co_kwonlyargcount
