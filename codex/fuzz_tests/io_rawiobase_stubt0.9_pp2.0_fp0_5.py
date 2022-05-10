import io
class File(io.RawIOBase):
    def __init__(self):
        self.file = open("writefile.text","w")

    def write(self, data):
        self.file.write(data);
f1 = File()
f1.write("hi")
