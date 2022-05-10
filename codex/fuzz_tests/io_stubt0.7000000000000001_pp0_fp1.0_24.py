import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

import pickle

class C:
    def __init__(self, a=1):
        self.a = a
    def __eq__(self, other):
        return self.a == other.a

c = C()
c.b = c
cstr = pickle.dumps(c)
c2 = pickle.loads(cstr)

print(c2.a)
print(c2.b.a)
print(c2.b.b.a)

class MyObject:
    def my_method(self):
        pass

assertMyObject = MyObject()
assertMyObject.my_method()

# str-subclass
class StrSubclass(str): pass
s = StrSubclass("hello")
print(s.upper())

# bytes-subclass
class BytesSubclass(bytes): pass
b = BytesSubclass(b"hello")
print(b.upper())
