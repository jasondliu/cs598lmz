import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n=-1):
        return self.file.read(n)
    def readinto(self, b):
        data = self.file.read(len(b))
        n = len(data)
        try:
            b[:n] = data
        except TypeError as err:
            import array
            if not isinstance(b, array.array):
                raise err
            b[:n] = array.array(b'b', data)
        return n

def open(file, mode="r"):
    if mode not in ("r", "w"):
        raise ValueError("invalid mode: %r" % mode)
    return File(file)

def main():
    import sys
    import binascii
    with open(sys.argv[1], "rb") as f:
        while True:
            chunk = f.read(16)
            if len(chunk) == 0:
                break
            print(binascii.
