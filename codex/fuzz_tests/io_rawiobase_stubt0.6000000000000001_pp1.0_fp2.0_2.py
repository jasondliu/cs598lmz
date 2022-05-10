import io
class File(io.RawIOBase):
    def __init__(self, file: io.IOBase):
        self.file = file

    def readinto(self, b: bytearray) -> int:
        view = memoryview(b)
        n = self.file.readinto(view)
        return n

file = File(io.BytesIO(b'abc'))
b = bytearray(10)
n = file.readinto(b)
print(b, n)

# 创建一个文件对象，并且指定它的打开模式为 rb
# file = open('/tmp/spam.bin', 'rb')
# file = open('/tmp/spam.bin')
# file = open('/tmp/spam.bin', 'r')
# file = open('/tmp/spam.bin', 'rb')
# file = open('/tmp/spam.bin', 'r', encoding='utf8')
# file = open('/tmp/sp
