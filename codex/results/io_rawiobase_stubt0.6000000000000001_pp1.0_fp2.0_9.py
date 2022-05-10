import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.fd = open(path, 'rb')

    def read(self, size):
        return self.fd.read(size)

    def readinto(self, b):
        data = self.read(len(b))
        n = len(data)
        try:
            b[:n] = data
        except TypeError as err:
            import array
            if not isinstance(b, array.array):
                raise err
            b[:n] = array.array('b', data)
        return n

    def close(self):
        return self.fd.close()

print(File(__file__).read())

print()

# 可以用这种方式创建一个只读的缓冲区对象（它是一个bytes-like object）:
import mmap
with open('lorem.txt', 'r') as f:
    m = mmap.mmap
