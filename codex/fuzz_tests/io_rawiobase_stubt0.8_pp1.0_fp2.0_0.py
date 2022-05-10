import io
class File(io.RawIOBase):
    def __init__(self):
        self.position = 0

    def seek(self, position):
        self.position = position

    def read(self, size):
        print(size)
        return bytes(range(self.position, self.position + size))

    def fileno(self):
        pass


# 打开文件
file = File()

# 读取文件信息
file.read(10)
# 读取文件的一部分
file.seek(2)
file.read(3)

# 读取文件的一部分
file.seek(10)
file.read(3)
