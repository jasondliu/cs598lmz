import types
types.MethodType(lambda self: None, None, None)

#  pylint: disable=unused-argument
def _mock_method(*args, **kwargs):
    pass

Mock = mock.Mock
patch = mock.patch
PropertyMock = mock.PropertyMock

def mock_open(mock=None, read_data=''):
    if mock is None:
        mock = Mock()

    handle = Mock()
    handle.write.return_value = None
    handle.read.return_value = read_data
    handle.__enter__.return_value = handle

    mock.return_value.__enter__.return_value = handle
    mock.return_value.__exit__.return_value = None

    return mock
