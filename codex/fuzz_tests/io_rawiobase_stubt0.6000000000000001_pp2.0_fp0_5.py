import io
class File(io.RawIOBase):
    def readinto(self, b):
        n = len(b)   # 读多少个字节
        print('b的长度是：', n)
        i = 0
        while i < n:
            # 这里没有考虑到文件结束的情况
            b[i:i+1] = self.read(1)
            i += 1
        return n

f = File()
b = bytearray(2)
f.readinto(b)
print(b)

print('*'*50)

class File(io.RawIOBase):
    def readinto(self, b):
        n = len(b)   # 读多少个字节
        print('b的长度是：', n)
        i = 0
        while i < n:
            # 这里没有考虑
