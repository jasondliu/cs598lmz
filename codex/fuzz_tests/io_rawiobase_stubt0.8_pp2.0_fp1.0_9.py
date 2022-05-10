import io
class File(io.RawIOBase): pass
class FileInput(io.FileIO): pass
class StringIO(io.StringIO): pass
class TextIOWrapper(io.TextIOWrapper): pass

# io.SEEK_* constants
SEEK_SET = io.SEEK_SET
SEEK_CUR = io.SEEK_CUR
SEEK_END = io.SEEK_END

# io.DEFAULT_BUFFER_SIZE
DEFAULT_BUFFER_SIZE = io.DEFAULT_BUFFER_SIZE

try:
    _is_string = unicode
except NameError:
    _is_string = str


class BytesIO(io.BytesIO):
    """
    BytesIO([initial_bytes]) -> object

    A file-like object for reading or writing bytes data.

    While StringIO only handles unicode strings, BytesIO can handle arbitrary
    bytes.

    Note that this class is not suitable for accepting binary data from a
    socket or from a file opened in binary mode. In those cases, use
    os.fdopen() to create a real file object.

    Methods:
