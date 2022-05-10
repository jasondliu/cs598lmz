fn = lambda: None
gi = (i for i in ())
fn.__code__ = mock.MagicMock()


def test_tot():
    """
    Test that the code is marked as "tot".
    """
    assert hasattr(sorted(fn.__code__.co_flags), 'tot')


def test_co_lnotab():
    """
    Test that the lineno table is b''.
    """
    assert fn.__code__.co_lnotab == b''


def test_co_firstlineno():
    """
    Test that the first line-number is 1.
    """
    assert fn.__code__.co_firstlineno == 1


def test_co_lnotab():
    """
    Test that the lineno table is b''.
    """
    assert fn.__code__.co_lnotab == b''


def test_co_argcount():
    """
    Test that the number of arguments is 0.
    """
    assert fn.__code__.co_argcount == 0


def test_co_nameditems():
    """
    Test that there are no named items
