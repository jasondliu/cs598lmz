import io
class File(io.RawIOBase):
    def __init__(self, filename, mode="rb"):
        self.filename = filename
        self.mode = mode
        self.fp = None
        self.fp_offset = 0
        self.closed = False

        # open the file, then call our super constructor
        self.fp = open(self.filename, self.mode)

        super().__init__()

    def close(self):
        if self.closed:
            return
        if self.fp is not None:
            self.fp.close()
        self.closed = True

    def __del__(self):
        self.close()

    def seekable(self):
        return True

    def readable(self):
        return True

    def tell(self):
        return self.fp_offset

    def seek(self, offset, whence=os.SEEK_SET):
        if whence == os.SEEK_SET:
            self.fp_offset = offset
        elif whence == os.SEEK_CUR:
            self.fp_offset += offset
        elif whence == os.SEEK
