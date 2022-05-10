import io
class File(io.RawIOBase):
    def write(self, data):
        pass


class Readable(io.RawIOBase):
    def read(self, size=-1):
        pass


class Writable(io.RawIOBase):
    def write(self, data):
        pass


class ReadWrite(Readable, Writable):
    pass


class ReadWriteSeekable(ReadWrite, io.RawIOBase):
    def seek(self, offset, whence=0):
        pass

    def tell(self):
        pass


class ReadWriteSeekableTellable(ReadWriteSeekable):
    def tell(self):
        pass


class ReadWriteSeekableTellableNoRawIOBase(ReadWriteSeekable):
    def tell(self):
        pass

    def readable(self):
        pass

    def writable(self):
        pass

    def seekable(self):
        pass


class ReadableNoRawIOBase(Readable):
    def readable(self):
        pass


class WritableNoRawIOBase(Writable):
    def writable(self):

