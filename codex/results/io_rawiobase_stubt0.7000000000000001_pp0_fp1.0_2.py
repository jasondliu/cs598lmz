import io
class File(io.RawIOBase):
    def read(self, size=-1):
        # Implement reading.
        pass

    def write(self, b):
        # Implement writing.
        pass

file = File()
print(file.read())
