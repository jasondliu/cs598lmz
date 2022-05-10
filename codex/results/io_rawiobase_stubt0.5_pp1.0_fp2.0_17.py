import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f

    def readinto(self, b):
        n = len(b)
        s = self.f.read(n)
        b[:len(s)] = s
        return len(s)

    def write(self, b):
        self.f.write(b)
        return len(b)

def open(filename, mode="r"):
    if mode[0] not in "rwa":
        raise ValueError("invalid mode %r" % mode)
    return File(open(filename, mode))

def main():
    with open("/etc/hosts") as f:
        print(f.read(16))
    f = open("/etc/hosts", "wb")
    f.write(b"abc")

if __name__ == "__main__":
    main()
