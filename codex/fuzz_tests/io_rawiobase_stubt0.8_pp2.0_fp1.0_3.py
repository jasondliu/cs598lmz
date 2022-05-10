import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f

    def read(self, n=-1):
        return self.f.read(n)

    def readinto(self, b):
        data = self.f.read(len(b))
        n = len(data)
        try:
            b[:n] = data
        except TypeError as err:
            import array
            if not isinstance(b, array.array):
                raise err
            b[:n] = array.array('b', data)
        return n

f = open('README.txt')
print(type(File(f)))

# 此外，如果你想要定义的是一个通用的接口或者是想要确保你的代码可以同时工作在Python 2和3中，
# 可以使用 io.IOBase 来作
