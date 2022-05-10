import io
class File(io.RawIOBase):
    def readinto(self, b):
        # ...
        return 0

mysock = File()
print(mysock.readinto(b"aaa"))

# 上面的例子只是简单的演示了这样的自定义文件对象的创建方式，
# 但是它在实际使用的时候会有各种问题。
# 比如，对于某些方法会抛出 NotImplementError 异常，
# 而对于另一些方法，比如 readinto() ，它返回的是错误的值。
# 读者可以查看 io 模块中的 RawIO
