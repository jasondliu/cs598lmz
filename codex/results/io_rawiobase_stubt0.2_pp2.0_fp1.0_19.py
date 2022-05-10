import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n)
    def write(self, b):
        return self.f.write(b)
    def close(self):
        return self.f.close()

def test():
    f = File(open('test.txt', 'rb'))
    print(f.read())
    f.close()

if __name__ == '__main__':
    test()
