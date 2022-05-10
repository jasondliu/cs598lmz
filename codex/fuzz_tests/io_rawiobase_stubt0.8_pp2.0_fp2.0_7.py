import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
    def readable(self):
        return True
    def writeable(self):
        return True
    def fileno(self):
        return self.name

f = File("test.txt")
print(f.readable())
print(f.writeable())
print(f.fileno())

def __enter__(self):
    pass
    #return self
def __exit__(self, *args):
    pass
    #return True
