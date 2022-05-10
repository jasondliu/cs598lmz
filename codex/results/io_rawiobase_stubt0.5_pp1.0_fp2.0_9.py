import io
class File(io.RawIOBase):
    def __init__(self, fd):
        self.fd = fd
    def fileno(self):
        return self.fd
    def read(self, n=None):
        return os.read(self.fd, n)
    def write(self, b):
        return os.write(self.fd, b)
    def close(self):
        return os.close(self.fd)
    @staticmethod
    def open(filename, mode='r'):
        return File(os.open(filename, mode))

def f(x):
    return x * x

def main():
    f = File.open("./test.txt", "w")
    print(f.write("hello"))
    f.close()
    print(f.read())
    print(f.read())
    f.close()
    print(f.read())

if __name__ == '__main__':
    main()
