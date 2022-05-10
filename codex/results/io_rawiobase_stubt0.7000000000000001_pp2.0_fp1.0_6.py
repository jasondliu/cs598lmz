import io
class File(io.RawIOBase):
    def __init__(self, fd):
        self.fd = fd

    def readinto(self, b):
        return self.fd.readinto(b)

buf = bytearray(10)
file = File(open('/dev/urandom', 'rb'))
file.readinto(buf)
print(buf)

# 调用close()会导致内部文件描述符(fd)被关闭
file.close()

# 调用close()会导致内部文件描述符(fd)被关闭
file.close()

# 调用close()会导致内部文件描述符(fd)被关闭
file.close()
