import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.file = None
    def open(self):
        self.file = open(self.name, 'rb')
    def close(self):
        if self.file:
            self.file.close()
            self.file = None
    def readable(self):
        return True
    def readinto(self, b):
        return self.file.readinto(b)

f = File('./hello.txt')
f.open()
print(f.readinto(b'123'))
f.close()
