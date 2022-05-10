import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.file = io.open(name, mode='rb')
    def readable(self):
        return True
    def readinto(self, b):
        return self.file.readinto(b)
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)
    def close(self):
        return self.file.close()
</code>
Now we can use it like this to read the file in chunks of size <code>n</code> bytes:
<code>f = File('test.txt')

while True:
    chunk = f.read(n)
    if not chunk:
        break
    print(chunk)
</code>

