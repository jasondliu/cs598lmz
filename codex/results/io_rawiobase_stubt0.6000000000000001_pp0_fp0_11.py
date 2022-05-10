import io
class File(io.RawIOBase):
    def read(self, n=-1):
        # ...
        return b""

f = File()
f.read()

# 可以实现的方法有：
# read, readinto, write, seek, truncate, tell, fileno,
# readable, writable, seekable, closed
#
# 可以继承io.IOBase类实现其他方法
#
# io.IOBase是抽象类，不能直接实例化
f = io.IOBase()

# 可以使用io.RawIOBase，io.BufferedIOBase类继承
# RawIOBase
# readinto, readable, writable, seekable, fileno
# BufferedIOBase
# read, write, seek, truncate, tell, fileno,
# readable, writable, seekable, closed
