import io
class File(io.RawIOBase):
    def __init__(self):
        self.buf = io.BytesIO()
        self.pos = 0

    def read(self, size=-1):
        assert self.buf.tell() == self.pos
        return self.buf.read(size)

    def write(self, data):
        assert self.buf.tell() == self.pos
        self.buf.write(data)
        self.pos += len(data)
        return len(data)

    def seek(self, offset, whence=0):
        if whence == io.SEEK_SET:
            new_pos = offset
        elif whence == io.SEEK_CUR:
            new_pos = self.buf.tell() + offset
        elif whence == io.SEEK_END:
            new_pos = self.buf.seek(0, 2) + offset
        else:
            raise ValueError("Unknown whence value %d" % whence)
        if new_pos < 0:
            raise ValueError("Invalid offset %d" % new_pos)
        self.buf.seek(new_
