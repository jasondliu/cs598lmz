fn = lambda: None
gi = (i for i in ())
fn.__code__ = [lambda: None]


# Expose the new mocks to PyPy's interpreter.
import sys
glob = sys.modules.get('__builtin__').__dict__
for k in locals().keys():
    if k.startswith('mock_') and k != 'mock_object':
        glob[k] = locals()[k]

# Remove old mocks from the interpreter.
del mock_object
del Rpbc


def test_objects_are_mocks():
    for k, v in locals().items():
        if k.startswith('mock_') and k != 'mock_object':
            assert isinstance(v, MockObject)


def test_mocks_repr():
    # Check that we get the name in the repr: it's for more
    # debuggability
    for v in values:
        r = repr(v)
        assert 'object' in r or 'instance' in r


def test_mock_str():
    o = object()
    assert o.__str__ == o
    assert o.__
