import bz2
# Test BZ2Decompressor's tell()/seek() implementation, using a
# non-seekable file.

class NonSeekableFile(object):
    def __init__(self, data):
        self.data = data
        self.offset = 0

    def read(self, size=None):
        if size is None:
            size = len(self.data) - self.offset
        if self.offset >= len(self.data):
            return b''
        result = self.data[self.offset:self.offset+size]
        self.offset += size
        return result

    def tell(self):
        return self.offset

    def seek(self, offset, whence=0):
        # Simulate a file that can't be seeked
        if whence == 1:
            raise ValueError('cannot seek from current position')
        if whence == 2:
            raise ValueError('cannot seek from end of file')
        if offset < 0:
            raise ValueError('offset cannot be negative')
        raise IOError(errno.ESPIPE, 'No seeking on this file type')

    def
