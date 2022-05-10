import io
# Test io.RawIOBase for presence of readinto method.
# NOTE(gazay): Python 2.6 io.RawIOBase is NOT a new-style class.
if hasattr(io.RawIOBase, 'readinto'):
    from io import RawIOBase
else:
    from collections import UserString  # noqa
    class RawIOBase(UserString):
        pass

from django.core.files.base import File, ContentFile


__all__ = ['TemporaryUploadedFile', 'TemporaryUploadedFileError']


class TemporaryUploadedFileError(AttributeError):
    pass


class TemporaryUploadedFile(RawIOBase):
    DEFAULT_CHUNK_SIZE = 64 * 2 ** 10

    def __init__(self, name, content_type, size, charset):
        self.file = tempfile.TemporaryFile()

        self.name = name
        self.content_type = content_type
        self.size = size
        self.charset = charset
        self.closed = False
        self.blksize = self.DEFAULT_CHUNK_
