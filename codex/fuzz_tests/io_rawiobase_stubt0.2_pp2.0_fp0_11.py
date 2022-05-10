import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n=-1):
        return self.file.read(n)
    def write(self, b):
        return self.file.write(b)
    def close(self):
        return self.file.close()

def test(file):
    f = File(file)
    print(f.read())

test(open('test.txt', 'r'))
</code>

