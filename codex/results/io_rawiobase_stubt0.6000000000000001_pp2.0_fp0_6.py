import io
class File(io.RawIOBase):
    def __init__(self, path):
        self._file = open(path, 'rb')

    def read(self, size):
        return self._file.read(size)

    def close(self):
        self._file.close()

# Create a file object
file = File('data.txt')

print(file.read(3))

print(file.read(3))

print(file.read(3))

print(file.read(3))

file.close()

# Create a file object
file = File('data.txt')

# Read all the data
print(file.read())

file.close()

# Create a file object
file = File('data.txt')

# Read all the data
print(file.read().decode('utf-8'))

file.close()

# Create a file object
file = File('data.txt')

# Read all the data
print(file.read().decode('utf-8'))

# Read the first 3 characters
print(file.read(3).
