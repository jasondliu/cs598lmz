import io
class File(io.RawIOBase):
    def write(self, b):
        print(b)
f = File()
f.write(b"hello")

# 这个类的实例是一个文件对象，但是它并不是一个真正的文件对象，而是一个模拟的文件对象。
# 它只是实现了文件对象的一个子集，并且只是简单地将输入内容打印出来。

# 如果你想要实现一个更加通用的文件对象，你可以继承 io.RawIOBase 类，并且实
