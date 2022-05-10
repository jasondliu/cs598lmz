import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path = path

    def read(self, size):
        with open(self.path, 'rb') as f:
            return f.read(size)

    def readline(self, size):
        with open(self.path, 'rb') as f:
            return f.readline(size)

    def readlines(self, size):
        with open(self.path, 'rb') as f:
            return f.readlines(size)

def main():
    f = File("test.txt")
    print(f.read(10))
    print(f.readline(10))
    print(f.readlines(10))

if __name__ == '__main__':
    main()
