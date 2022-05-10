import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.offset = 0
    def read(self, n=-1):
        self.file.seek(self.offset)
        buf = self.file.read(n)
        self.offset = self.file.tell()
        return buf

def main():
    file = open("/home/joe/Desktop/test.txt", 'rb')
    f = File(file)
    print(f.read(5))
    print(f.read(5))

if __name__ == '__main__':
    main()
