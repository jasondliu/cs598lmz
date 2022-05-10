import io
class File(io.RawIOBase):
    def __init__(self, path, mode="r"):
        self.path = path
        self.mode = mode

    def read(self):
        if 'r' in self.mode:
            return open(self.path, self.mode).read()
        return None
    def write(self, data):
        if 'w' in self.mode:
            with open(self.path, self.mode) as f:
                f.write(data)
            return True
        return False

file1 = File("data.txt", "r")
print(file1.read())
file2 = File("data2.txt", "w")
file2.write("hola")
