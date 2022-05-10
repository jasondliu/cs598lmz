import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.offset = 0

    def readinto(self, b):
        if self.closed:
            raise ValueError("I/O operation on closed file.")

        l = len(b) # No need to call len() again.
        chunk = self.file.read(self.offset, l)
        b[:len(chunk)] = chunk
        self.offset += len(chunk)
        return len(chunk)

    def seekable(self):
        return True

    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_CUR:
            offset += self.offset
        elif whence == io.SEEK_END:
            offset += self.file.size()
        self.offset = offset
        return self.offset

    def tell(self):
        return self.offset

    def readable(self):
        return True

    def writable(self):
        return False

    def flush(self):
        pass

    def close
