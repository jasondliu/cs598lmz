import weakref
import yaml

if PY3:
    from urllib.parse import urlparse
else:
    from urlparse import urlparse

from . import _libcloud_file

__all__ = [
    "File",
    "FileChunkIterator",
    "FileIterator",
    "FileUploadChunkIterator",
    "ExistingFile",
    "FileUpload",
    "StreamFile"
]


def _open(name, mode):
    try:
        return open(name, mode)
    except IOError as e:
        raise File.IOError(e)


class FileChunkIterator(_libcloud_file.FileChunkIterator):
    def __init__(self, file_path, chunk_size, open_file=_open):
        super(FileChunkIterator, self).__init__(file_path, chunk_size)
        self.open_file = open_file

    def open(self, file_path, mode):
        return self.open_file(file_path, mode)


