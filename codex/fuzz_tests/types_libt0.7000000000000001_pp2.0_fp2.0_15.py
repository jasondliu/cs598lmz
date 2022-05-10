import types
types.SimpleNamespace

from types import SimpleNamespace

def test_get_non_existing_key():
    a = SimpleNamespace()
    with pytest.raises(AttributeError):
        a.b


def test_create_non_existing_key():
    a = SimpleNamespace()
    a.b = 1
    assert a.b == 1


def test_non_existing_key_is_not_visible_in_dir():
    a = SimpleNamespace()
    a.b = 1
    assert 'b' not in dir(a)


def test_non_existing_key_is_visible_in_vars():
    a = SimpleNamespace()
    a.b = 1
    assert 'b' in vars(a)


def test_non_existing_key_is_visible_in_vars_not_in_dir_when_using_from_import():
    from types import SimpleNamespace
    a = SimpleNamespace()
    a.b = 1
    assert 'b' in vars(a)


def test_non
