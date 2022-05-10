import io
class File(io.RawIOBase):
    def readinto(self, b):
        n = len(b)
        b[:] = self.read(n)
        return n

f = File()
b = bytearray(10)
n = f.readinto(b)
print(n, b)

#Using memoryview
import array
numbers = array.array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(len(memv))
print(memv[0])
memv_oct = memv.cast('B')
print(memv_oct.tolist())
memv_oct[5] = 4
print(numbers)

#Delegating Iteration
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []
    def __repr__(self):
        return 'Node({!r})'.format(self._value)
    def add_child(self, node):
        self._children.append(node)
    def __iter__(
