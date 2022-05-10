import io
class File(io.RawIOBase):
    '''
    A file-like object on top of a Blob.
    '''
    def __init__(self, blob):
        '''
        :param blob: A blob-like object.
        '''
        self._blob = blob

    def readable(self):
        return True
    def readinto(self, b):
        l = len(b)
        data = self._blob.read(l)
        if data is None: return 0
        b[:len(data)] = data
        return len(data)

    def seekable(self):
        return True
    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self._blob.seek(offset, 0)
        elif whence == io.SEEK_CUR:
            self._blob.seek(offset, 1)
        elif whence == io.SEEK_END:
            self._blob.seek(offset, 2)
        else:
            raise ValueError("invalid whence (%r, should be
