import io
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        self.fp = open(filename, mode, encoding="CP437")

    def close(self):
        self.fp.close()

    def writable(self):
        return True
    def readable(self):
        return True
    def writelines(self, lines):
        self.fp.writelines(lines)
    def readlines(self):
        return self.fp.readlines()
    def flush(self):
        self.fp.flush()
    def read(self, n):
        return self.fp.read(n)
    def write(self, b):
        self.fp.write(b)
    def seek(self, pos, whence=0):
        return self.fp.seek(pos, whence)
    def tell(self):
        return self.fp.tell()

if __name__ == "__main__":
    f = File("test.txt", "rb+")
    f.write("Hello, world!")
    f.seek(0x3)
    print(f.
