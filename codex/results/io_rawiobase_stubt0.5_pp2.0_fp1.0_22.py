import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.file = None
    def open(self):
        self.file = open(self.name, 'r')
    def read(self, size=-1):
        return self.file.read(size)
    def close(self):
        self.file.close()

file = File('file.txt')
file.open()
print(file.read())
file.close()

# with
with File('file.txt') as file:
    print(file.read())

# context manager
class File:
    def __init__(self, name):
        self.name = name
        self.file = None
    def __enter__(self):
        self.file = open(self.name, 'r')
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with File('file.txt') as file:
    print(file.read())

# context manager as decorator
