import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.file = None
    def open(self):
        self.file = open(self.name, "rb")
    def close(self):
        if self.file:
            self.file.close()
            self.file = None
    def readinto(self, b):
        return self.file.readinto(b)
    def __del__(self):
        self.close()

f = File("test.txt")
f.open()
b = bytearray(10)
n = f.readinto(b)
print(b)
print(n)
f.close()

# class File(io.RawIOBase):
#     def __init__(self, name):
#         self.name = name
#         self.file = None
#     def open(self):
#         self.file = open(self.name, "rb")
#     def close(self):
#         if self.file:
#             self.file.close()
#             self
