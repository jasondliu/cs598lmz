import io
class File(io.RawIOBase):
    #...
    def readinto(self, b):
        #...
        return n

f = open("test.txt", "rb")
buf = bytearray(10)
f.readinto(buf)
f.close()
print buf

with open("test.txt", "rb") as f:
    buf = bytearray(10)
    f.readinto(buf)
    print buf
