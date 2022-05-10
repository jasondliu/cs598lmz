fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi


def test_get_code_data():
    assert get_code_data(fn) == gi


def test_get_code_data_with_class():
    class Fn:
        def __call__(self):
            pass

    fn = Fn()
    assert get_code_data(fn) == Fn.__call__.__code__


def test_get_code_data_with_instance():
    class Fn:
        def __call__(self):
            pass

    fn = Fn()
    fn.__code__ = gi

    assert get_code_data(fn) == gi


def test_get_code_data_with_code():
    code = gi.__code__
    assert get_code_data(code) == code


def test_get_code_data_with_non_callable():
    assert get_code_data(gi) is None


def test_get_code_data_with_non_code():
    assert get_code_data(gi) is None


def test_get_code
