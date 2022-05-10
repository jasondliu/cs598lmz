import io
class File(io.RawIOBase):
    def __init__(self, fd):
        self.fd = fd
    def readinto(self, b):
        return self.fd.readinto(b)
    def write(self, b):
        return self.fd.write(b)
    def fileno(self):
        return self.fd.fileno()

def main():
    fd = os.open("/tmp/test", os.O_RDWR)
    f = File(fd)
    f.write(b"hello")
    f.seek(0)
    print(f.read())

if __name__ == "__main__":
    main()
