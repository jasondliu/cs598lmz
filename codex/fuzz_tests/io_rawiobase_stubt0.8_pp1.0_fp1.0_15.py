import io
class File(io.RawIOBase):
    ...

try:
    from _io import FileIO
except ImportError:
    FileIO = File

try:
    from _io import BufferedIOBase
except ImportError:
    BufferedIOBase = File

try:
    from _io import BytesIO
except ImportError:
    BytesIO = io.BytesIO

# The following is copied directly from the Python-3.5.1 standard library.
#
# The comments have been removed, and the exception names have been renamed to match those
# used in six.reraises.
try:
    from _io import UnsupportedOperation
except ImportError:
    _unsupported_operation_doc = """\
    This operation currently not supported by the IO implementation."""

    class UnsupportedOperation(ValueError):
        __doc__ = _unsupported_operation_doc

try:
    from _io import BlockingIOError
except ImportError:
    _blocking_io_error_doc = """\
    A write could not be completed without blocking."""

    class BlockingIOError(IOError):
        __doc__ =
