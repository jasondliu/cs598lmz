import mmap

from . import const
from . import util
from . import get_default_logger
from .util import OpenMode

__all__ = ['File', 'FileBackend', 'FileBackendManager']

logger = get_default_logger()


class File(object):
    def __init__(self, backend, path, mode=OpenMode.READ, offset=0, size=-1):
        self._backend = backend
        self._path = path
        self._mode = mode
        self._offset = offset
        self._size = size
        self._pos = 0
        self._closed = False

    @property
    def path(self):
        return self._path

    @property
    def mode(self):
        return self._mode

    @property
    def offset(self):
        return self._offset

    @property
    def size(self):
        return self._size

    @property
    def closed(self):
        return self._closed

    @property
    def pos(self):
        return self._pos

    def seek(self, offset
