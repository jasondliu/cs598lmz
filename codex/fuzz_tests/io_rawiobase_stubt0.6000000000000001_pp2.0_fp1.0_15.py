import io
class File(io.RawIOBase):
    def __init__(self, file_obj):
        self.file_obj = file_obj
    def readable(self):
        return True
    def readinto(self, b):
        data = self.file_obj.read(len(b))
        n = len(data)
        b[:n] = data
        return n

f = open('../data/data.txt', 'rb')
buf = bytearray(1024)
f.readinto(buf)
print(buf)
f.close()

f = File(open('../data/data.txt', 'rb'))
buf = bytearray(1024)
f.readinto(buf)
print(buf)
f.close()

# 在文件上使用操作系统提供的缓存机制 使用mmap模块来精确控制缓存的使用
# 这个模
