import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r'):
        self.name = name
        self.mode = mode

    def close(self):
        # Flush and close the file.
        self.flush()
        return super().close()

file = File('demo.txt', 'w')
file.write(b'0123456789abcdef')
print(file.tell())  # 16
file.seek(-3, os.SEEK_CUR)
print(file.tell())  # 13
print(file.read(1))  # b'd'

file = File('demo.txt', 'r')
print(file.read(1))  # b'0'

file.close()
