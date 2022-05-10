import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self.filename = filename
        self.positions = [0]
        self.file = open(filename, 'w')
    def seekable(self):
        return True
    def writable(self):
        return True
    def readable(self):
        return True
    def write(self, data):
        self.file.write(data)
        return len(data)
    def seek(self, offset, whence=io.SEEK_CUR):
        if whence == io.SEEK_CUR:
            offset += self.positions[-1]
        elif whence == io.SEEK_END:
            offset += self.positions[0]
        elif whence == io.SEEK_SET:
            pass
        else:
            raise ValueError("Invalid value for 'whence'")
        self.positions.append(offset)
    def tell(self):
        return self.positions[-1]
    def close(self):
        self.file.close()

for i in range(0
