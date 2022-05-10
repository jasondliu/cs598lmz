import weakref

from . import _base
from . import _compat
from . import _util

_logger = _compat.logging.getLogger(__name__)

_DEFAULT_MAX_SIZE = 1024 * 1024 * 10  # 10 MB

_DEFAULT_MAX_SIZE_FOR_IN_MEMORY_DATA = 1024 * 1024 * 1  # 1 MB


class _Data(object):
    """
    A wrapper for data.
    """

    def __init__(self, data, content_type, filename, size):
        self._data = data
        self._content_type = content_type
        self._filename = filename
        self._size = size

    @property
    def data(self):
        return self._data

    @property
    def content_type(self):
        return self._content_type

    @property
    def filename(self):
        return self._filename

    @property
    def size(self):
        return self._size


class _File(object):
    """
    A wrapper for file.
    """


