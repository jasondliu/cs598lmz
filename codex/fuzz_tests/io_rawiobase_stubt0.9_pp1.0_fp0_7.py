import io
class File(io.RawIOBase):
    def __init__(self, fh):
        if not isinstance(fh, io.RawIOBase):
            fh = io.open(fh, 'rb')
        self.fh = fh

        self.start = self.fh.tell()
        self.seekable = self.fh.seekable()

        # XXX: RawIOBase doesn't have a name, we don't really have anything
        # else to use as a name though, so we just mutate internal attributes
        self.name = self.fh.name
        self.mode = self.fh.mode

    def tell(self):
        return self.fh.tell() - self.start

    def seek(self, offset, whence=0):
        return self.fh.seek(self.fix_offset(offset, whence))

    def readable(self):
        return self.fh.readable()

    def writable(self):
        return self.fh.writable()

    def seekable(self):
        return self.fh.seekable()

    def close(
