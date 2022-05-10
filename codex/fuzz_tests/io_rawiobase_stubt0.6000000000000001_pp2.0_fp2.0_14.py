import io
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    def read(self, size=-1):
        #print("reading from file")
        return open(self.filename, self.mode).read()
    def write(self, data):
        #print("writing to file")
        open(self.filename, self.mode).write(data)

print(File("test.txt", "r").read())
print(File("test.txt", "w").write("test"))
