fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi


def test_code_is_not_iterable():
    with pytest.raises(TypeError):
        _ = list(fn.__code__)


def test_code_iter_is_iterable():
    assert list(code_iter(fn)) == ['i']


def test_code_iter_extra_arg():
    with pytest.raises(TypeError):
        _ = list(code_iter(fn, 1))


def test_code_iter_is_not_iterable():
    with pytest.raises(TypeError):
        _ = list(code_iter(None))


def test_code_iter_keyword_arg():
    with pytest.raises(TypeError):
        _ = list(code_iter(foo=1))


def test_code_iter_is_generator():
    assert inspect.isgeneratorfunction(code_iter)


def test_code_iter_is_not_generator():
    assert not inspect.isgeneratorfunction(fn)
