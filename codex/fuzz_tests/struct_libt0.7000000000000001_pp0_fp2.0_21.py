import _struct
import _functools


def _mock_open(mock=None, read_data=''):
    """
    A helper function to create a mock to replace the use of `open`. It works for
    `open` called directly or used as a context manager.

    The `mock` argument is the mock object to configure. If `None` (the default)
    then a `MagicMock` will be created for you, with the API limited to methods or
    attributes available on standard file handles.

    `read_data` is a string for the `read` methoddlineine of the file handle to return.  This
    is an empty string by default.
    """
    def _readlines_side_effect(*args, **kwargs):
        if PY2:
            return read_data.splitlines(True)
        else:
            return mock.readlines(*args, **kwargs)

    def _enter(*args, **kwargs):
        if PY2:
            return _readline_side_effect
        else:
            return mock.__enter__(*args,
