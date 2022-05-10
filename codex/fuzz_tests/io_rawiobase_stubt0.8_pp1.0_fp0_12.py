import io
class File(io.RawIOBase):
    def __init__(self, raw):
        self.raw = raw
        self.name = "RawIO_{}".format(id(self))
        self.close_called = False
        self.pos = 0
        self.size = -1

    @property
    def closed(self):
        return self.close_called

    def fileno(self):
        raise io.UnsupportedOperation()

    def close(self):
        self.close_called = True

    def readable(self):
        return True

    def seekable(self):
        return True

    def writable(self):
        return True

    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            if offset < 0:
                raise ValueError("negative seek position {}".format(offset))
            self.pos = offset
        elif whence == io.SEEK_CUR:
            self.pos += offset
        elif whence == io.SEEK_END:
            if offset > 0:
                raise ValueError("seek beyond end
