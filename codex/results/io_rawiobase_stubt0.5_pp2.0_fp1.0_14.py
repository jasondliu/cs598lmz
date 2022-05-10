import io
class File(io.RawIOBase):
    def __init__(self, fobj):
        self.fobj = fobj
        self.encoding = 'utf-8'
    def read(self, n):
        return self.fobj.read(n).decode(self.encoding)
    def readinto(self, b):
        data = self.fobj.read(len(b))
        n = len(data)
        try:
            b[:n] = data
        except TypeError as err:
            import array
            if not isinstance(b, array.array):
                raise err
            b[:n] = array.array(b'b', data)
        return n
with open('/tmp/test.txt', 'rb') as f:
    f = File(f)
    print(f.read())

'''
seek()
    文件对象的 seek() 方法让你能够在文件的任意位置开始读取或写
