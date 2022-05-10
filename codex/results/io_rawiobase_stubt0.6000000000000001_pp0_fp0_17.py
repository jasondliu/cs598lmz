import io
class File(io.RawIOBase):
    """
    A file-like object to be used with the :class:`~boto3.s3.transfer.S3Transfer` class.
    This class provides a few additional methods to make it easier to work with
    S3 objects.
    """
    def __init__(self, s3, key, buffer_size=8388608, num_attempts=10):
        self._s3 = s3
        self._key = key
        self._buffer_size = buffer_size
        self._num_attempts = num_attempts
        self._pos = 0
        self._len = key.content_length

    def __repr__(self):
        return 's3transfer.s3.File(s3={0}, key={1})'.format(
            self._s3, self._key)

    def tell(self):
        return self._pos

    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_CUR:
            self._pos += offset
        elif whence == io.SEE
