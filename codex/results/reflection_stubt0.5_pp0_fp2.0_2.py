fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that __code__ is properly reset when the function is cleared
def test_clear():
    def f(): pass
    f.__code__ = None
    clear_code(f)
    assert f.__code__ is not None
    assert f.__code__.co_name == 'f'

def test_is_true():
    assert is_true(True)
    assert is_true(1)
    assert not is_true(False)
    assert not is_true(0)
    assert not is_true(None)

def test_is_none():
    assert is_none(None)
    assert not is_none(False)
    assert not is_none(0)
    assert not is_none(1)

def test_is_not_none():
    assert is_not_none(True)
    assert is_not_none(False)
    assert is_not_none(0)
    assert is_not_none(1)
    assert not is_not_none(None)

def test_is
