import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f

    def read(self):
        return self.f.read()

file = File(open('file.txt'))
print(file.read())
</code>

