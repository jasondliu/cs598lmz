import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self.filename = filename
        self.fh = None

    def read(self, n=-1):
        if self.fh is None:
            self.fh = open(self.filename, 'rb')
        return self.fh.read(n)

    def readable(self):
        return True


f = File('hello.txt')
print(f.read(4))
print(f.read(4))
print(f.read(4))

# f = open('hello.txt', 'rb')
# print(f.read(4))
# print(f.read(4))
# print(f.read(4))
#
# print('-' * 30)
#
# f = open('hello.txt', 'rb')
# print(f.read(4))
# print(f.read(4))
# print(f.read(4))
