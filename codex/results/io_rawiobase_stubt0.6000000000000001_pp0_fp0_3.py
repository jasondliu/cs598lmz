import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name

    def write(self, data):
        with open(self.name, 'w') as f:
            f.write(data)

# Create file object
f = File("file.txt")

# Use file object
f.write("Hello, world")
</code>

