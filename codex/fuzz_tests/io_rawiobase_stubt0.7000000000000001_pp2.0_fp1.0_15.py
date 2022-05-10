import io
class File(io.RawIOBase):
    def write(self, b):
        print("write",b)
    def read(self):
        print("read")

with open(r"C:\Users\JH\Desktop\test.txt", "w+") as f:
    f.write("hello world")
    f.read()

f = File()
f.write("hello".encode("utf-8"))
f.read()

class File(io.FileIO):
    def read(self):
        print(super().read())

#with open(r"C:\Users\JH\Desktop\test.txt", "rb") as f:
#    f.read(100)

f = File(r"C:\Users\JH\Desktop\test.txt")
f.read()

# https://docs.python.org/3/library/io.html
# https://docs.python.org/3/library/io.html#io.IOBase
