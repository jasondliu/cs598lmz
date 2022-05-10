import io
class File(io.RawIOBase):
    def read(self, arg=-1):
        print("read [%d]" % arg)
        return "hello"
    def write(self, arg):
        print("write [%s]" % arg)
f = File()
r = f.read(10)

print(r)
