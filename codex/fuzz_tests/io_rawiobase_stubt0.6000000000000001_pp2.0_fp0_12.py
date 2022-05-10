import io
class File(io.RawIOBase):
    def __init__(self):
        self.__value = 0

    def write(self, b):
        self.__value = b
        return len(b)

    def read(self):
        return self.__value

f = File()

f.write(b'hello world')
print(f.read())

f.write(b'1234567')
print(f.read())

f.write(b'1234567')
print(f.read())

#f.read()
