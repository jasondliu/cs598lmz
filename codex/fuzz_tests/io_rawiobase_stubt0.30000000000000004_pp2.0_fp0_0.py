import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def readinto(self, b):
        n = len(b) # b will be written to from offset 0
        view = memoryview(b).cast('B')
        while n > 0:
            buf = self.file.read(n)
            if not buf:
                break
            view[:len(buf)] = buf
            view = view[len(buf):] # slicing views is cheap
            n -= len(buf)
        return len(b) - n

def test():
    import sys
    f = File(sys.stdin.buffer)
    print(f.readinto(bytearray(10)))
    print(f.readinto(bytearray(10)))
    print(f.readinto(bytearray(10)))
    print(f.readinto(bytearray(10)))

if __name__ == '__main__':
    test()
