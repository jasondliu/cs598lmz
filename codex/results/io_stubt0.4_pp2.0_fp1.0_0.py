import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

# f.readinto(view)
view[0] = ord('A')

print(view)

# f = open("test.txt", "rb")
# view = memoryview(f.read(1))
# f.close()
# view[0] = ord('A')
# print(view)
#
# f = open("test.txt", "rb")
# view = memoryview(f.read(1))
# f.close()
# print(view)
#
# f = open("test.txt", "rb")
# view = memoryview(f.read(1))
# f.close()
# print(view)
