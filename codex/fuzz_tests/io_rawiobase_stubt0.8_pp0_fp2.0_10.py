import io
class File(io.RawIOBase):
    def read(self, size=None):
        return b"read"
    def readall(self):
        return b"readall"
with open('file.txt', 'w') as file:
    file.write("content\n")
with open('file.txt', 'r') as file:
    print("read(1):", file.read(1))
    file.seek(10)
    print("read(1):", file.read(1))
    print("read():", file.read())
    print("read(10):", file.read(10))
    file.seek(0)
    print("read():", file.read())
    print("readall():", file.readall())
    file.seek(0)
    print("readline():", file.readline())
    file.seek(0)
    print("readlines():", file.readlines())
    print("seekable():", file.seekable())
    print("readable():", file.readable())
    print("writeable():", file.writable())
    print("closed():", file.
