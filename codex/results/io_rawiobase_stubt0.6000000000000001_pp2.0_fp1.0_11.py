import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path = path
        self.f = open(self.path, 'rb')

    def read(self, n=-1):
        return self.f.read(n)

    def readable(self):
        return True

    def writable(self):
        return False

    def seekable(self):
        return True


f = File('/tmp/file')
print(f.readable())
print(f.writable())
print(f.seekable())
</code>
Output:
<code>True
False
True
</code>

