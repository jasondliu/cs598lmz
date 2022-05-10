import io
class File(io.RawIOBase):
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode

    def read(self, n=-1):
        with open(self.file_name, self.mode) as f:
            return f.read(n)

    def write(self, b):
        with open(self.file_name, self.mode) as f:
            return f.write(b)

f = File('file.txt', 'r')
f.read()

f = File('file.txt', 'w')
f.write('Hello World')

f = File('file.txt', 'r')
f.read()

f = File('file.txt', 'w')
f.write('Hello World')

f = File('file.txt', 'r')
f.read()
