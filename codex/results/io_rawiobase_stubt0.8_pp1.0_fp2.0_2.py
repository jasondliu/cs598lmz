import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file

    def readable(self):
        return True

    def readinto(self, b):
        n = len(b)
        data = self.file.read(n)
        n = len(data)
        b[:n] = data
        return n

f = open('myfile.txt', 'rb')
b = bytearray(100)
f = File(f)
f.readinto(b)

print(b)
</code>
Prints
<code>bytearray(b'data in file\nmore data\n')
</code>

