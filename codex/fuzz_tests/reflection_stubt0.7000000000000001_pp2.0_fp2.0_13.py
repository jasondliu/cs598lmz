fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = CodeType(
    0, 0, 0, 0, b"", b"", (), (), (), "", "", 0, b"")

with pytest.raises(ValueError):
    Mock()


def test_return_value():
    mock = Mock()
    mock.return_value = 3
    assert mock() == 3


def test_side_effect():
    mock = Mock()
    mock.side_effect = Exception
    with pytest.raises(Exception):
        mock()


def test_side_effect_generator():
    mock = Mock()
    mock.side_effect = (i for i in range(3))
    assert mock() == 0
    assert mock() == 1
    assert mock() == 2
    with pytest.raises(StopIteration):
        mock()


def test_call():
    mock = Mock()
    mock(1, 2, 3)
    assert mock.call_args == call(1, 2, 3)


def test_call_list():
    mock = Mock()
    mock
