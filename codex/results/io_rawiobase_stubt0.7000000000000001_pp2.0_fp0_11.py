import io
class File(io.RawIOBase):
    def __init__(self):
        self.content = b"aaaaaaaaaaaa"
        self.pos = 0

    def readinto(self, buffer):
        # print(buffer)
        # print(self.content)
        # print(self.pos)
        # print(len(self.content) - self.pos)
        # print(len(buffer))
        # print(self.content[self.pos:self.pos + len(buffer)])
        buffer[: len(self.content) - self.pos] = self.content[self.pos:self.pos + len(buffer)]
        self.pos += len(buffer)
        return len(buffer)

file = File()
print(file.readinto(bytearray(5)))
# print(file.readinto(bytearray(5)))
print(file.readinto(bytearray(5)))
print(file.readinto(bytearray(5)))
print(file.readinto(bytearray(5)))
