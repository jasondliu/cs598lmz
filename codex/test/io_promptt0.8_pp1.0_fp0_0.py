import io
# Test io.RawIOBase.read()

t1 = b'1'
t2 = b'2'
t3 = b'3'

class MyIO(io.RawIOBase):
    def read(self, n=-1):
        if n == 1:
            return t1
        elif n == 2:
            return t2
        elif n == 3:
            return t3
        elif n == -1:
            return t1+t2+t3
        return b''

    def read1(self, n=-1):
        return self.read(n)

    def readable(self):
        return True

print(MyIO().read(1))
print(MyIO().read(2))
print(MyIO().read(3))
print(MyIO().read())
# Test io.RawIOBase.readall()

t1 = b'1'
t2 = b'2'
t3 = b'3'

class MyIO(io.RawIOBase):
    def read(self, n=-1):
        if n == 1:
            return
