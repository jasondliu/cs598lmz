import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f

    def read(self, n):
        if n >= (1 << 31):
            buffer = bytearray(n)
            idx = 0
            while idx < n:
                batch_size = min(n - idx, 1 << 31 - 1)
                read = self.f.read(batch_size)
                buffer[idx:idx + len(read)] = read
                idx += len(read)
                if len(read) < batch_size:
                    break
            return bytes(buffer)
        return self.f.read(n)

    def seekable(self):
        return self.f.seekable()

    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET and offset >= 0:
            self.f.seek(offset)
            return
        if whence == io.SEEK_CUR and offset >= 0:
            self.f.seek(self.f.tell() + offset)
            return

