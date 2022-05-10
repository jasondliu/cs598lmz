fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__code__.co_filename

def test_filename():
    with pytest.raises(TypeError):
        fn.__code__.co_filename = 0
    with pytest.raises(TypeError):
        fn.__code__.co_filename = b'foo'
    with pytest.raises(TypeError):
        fn.__code__.co_filename = 'foo'
    fn.__code__.co_filename = 'bar'
    assert fn.__code__.co_filename == 'bar'

def test_name():
    with pytest.raises(TypeError):
        fn.__code__.co_name = 0
    with pytest.raises(TypeError):
        fn.__code__.co_name = b'foo'
    with pytest.raises(TypeError):
        fn.__code__.co_name = 'foo'
    fn.__code__.co_name = 'bar'
    assert fn.__code__.co_name == 'bar'

def
