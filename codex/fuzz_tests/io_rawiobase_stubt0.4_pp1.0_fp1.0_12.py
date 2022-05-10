import io
class File(io.RawIOBase):
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self, n=-1):
        with open(self.file_name, 'rb') as f:
            return f.read(n)

    def readable(self):
        return True

    def writable(self):
        return False

    def seekable(self):
        return False

def test():
    f = File('test.txt')
    print(f.read(10))

test()
</code>
The output is:
<code>b'1234567890'
</code>

