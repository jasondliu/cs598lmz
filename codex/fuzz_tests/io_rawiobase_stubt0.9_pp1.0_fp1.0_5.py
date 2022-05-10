import io
class File(io.RawIOBase):
    def __init__(self):
        self.position = 0
        self.data = b'1234567890' * 100
    def readinto(self, b):
        length = len(b)
        if self.position + length > len(self.data):
            length = len(self.data) - self.position
        b[:length] = self.data[self.position:self.position+length]
        self.position += length
        return length
    def write(self, bytes):
        print(bytes)
        return len(bytes)

file = File()
print(file.read(10), file.tell())
print(file.read(10), file.tell())
print(file.seek(10, io.SEEK_SET), file.tell())
print(file.read(10), file.tell())
print(file.seek(10, io.SEEK_END), file.tell())
print(file.read(10), file.tell())

file2 = io.BytesIO(b'1234567890' * 100)
print(file2
