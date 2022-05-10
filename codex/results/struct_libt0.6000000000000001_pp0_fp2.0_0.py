import _struct

from . import _file
from . import _file_types
from . import _helpers
from . import _io_utils
from . import _lib
from . import _py_utils
from . import errors


_FILE_TYPE_TO_READER_CLASS = {}
_FILE_HEADER_LENGTH = 4


class _ReaderBase(object):
  """Base class for reader."""

  def __init__(self, file_path, mode="rb"):
    """Create a Reader.

    Args:
      file_path: The file path.
      mode: The mode used to open the file, defaults to "rb".
    """
    self._file_path = file_path
    self._mode = mode
    self._file_handle = None
    self._file_type = None
    self._file_version = None
    self._file_header_length = _FILE_HEADER_LENGTH
    self._record_count = None
    self._record_count_offset = None
    self._record_count_length = None
    self._record_length =
