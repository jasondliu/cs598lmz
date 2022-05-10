import io
class File(io.RawIOBase):
    def __init__(self, name, mode="r"):
        self.name = name
        self.mode = mode

    def close(self):
        if self.mode[0] in 'wa':
            with open(self.name, 'w') as f:
                f.write(self.buffer)

    def fileno(self):
        return self

    def flush(self):
        pass

    def isatty(self):
        return True

    def readable(self):
        return True

    def writable(self):
        return True

    def seekable(self):
        return True

    def readinto(self, b):
        if self.mode[0] not in 'rw':
            raise IOError("File not open for reading")

        if isinstance(b, bytearray):
            byte_array = memoryview(b).cast('B')
            byte_array.extend(self.buffer)
        else:
            byte_array = b[:] + self.buffer
        return len(byte_array)

    def tell(self):

