import io
class File(io.RawIOBase):
    def read(self, n=-1):
        if n == -1:
            n = 2 ** 30

        if self.closed:
            raise ValueError("I/O operation on closed file")

        message = b"file.read macht was tolles"

        if n == 0:
            return b""

        range_end = min(len(message), self.tell() + n)
        message = message[self.tell():range_end]
        self.seek(range_end)
        return message
file = File()
print(file.read())
# file.read()
print(file.tell())
print(file.read())
print(file.tell())
print(file.read())
print(file.tell())
print(file.read())
file.close()
print(file.closed)

file = File()
print(file.readline())

class File(io.RawIOBase):
    def readable(self):
        return True
    def seekable(self):
        return True
    def writable(self):
        return True
    def
