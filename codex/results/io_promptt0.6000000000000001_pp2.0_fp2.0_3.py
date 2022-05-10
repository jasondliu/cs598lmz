import io
# Test io.RawIOBase subclass
#
# overload read() for various sizes
class MyIO(io.RawIOBase):
    def read(self, n=-1):
        if n == -1:
            return 'foo'
        elif n == 0:
            return ''
        else:
            return 'x' * n
# read()
print(MyIO().read())
print(MyIO().read(0))
print(MyIO().read(1))
print(MyIO().read(2))
print(MyIO().read(3))
# readinto()
b = bytearray(3)
print(MyIO().readinto(b))
print(b)
# readinto()
b = bytearray(2)
print(MyIO().readinto(b))
print(b)
# readinto()
b = bytearray(4)
print(MyIO().readinto(b))
print(b)
# Test read() from non-blocking RawIO
class NonBlockReader(io.RawIOBase):
    def readable(self):
        return True
    def readinto
