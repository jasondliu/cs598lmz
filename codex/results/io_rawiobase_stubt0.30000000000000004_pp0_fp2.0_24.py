import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def readable(self):
        return True
    def readinto(self, b):
        n = len(b)
        view = memoryview(b).cast("B")
        while n > 0:
            m = self.f.readinto(view)
            view = view[m:] # slicing views is cheap
            n -= m
            if m == 0:
                break
        return len(b) - n

f = File(open("/etc/passwd", "rb"))
print(f.read(5))

# 下面是一个使用io.RawIOBase基类的示例，它实现了一个简单的文件对象，
# 它可以从一个文件对象中读取数据，并且在读取
