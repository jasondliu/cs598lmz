import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
    def read(self):
        print('read')
        return '123'
    def tell(self):
        print('tell')
        return 1
    def seek(self, n):
        print('seek', n)
        return n

f = File('test')
print(f.read())
print(f.tell())
print(f.seek(10))
