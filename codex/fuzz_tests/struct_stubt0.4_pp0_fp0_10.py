from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<2s3s')
s.size

# Method Resolution Order
class A:
    def ping(self):
        print('ping:', self)

class B(A):
    def pong(self):
        print('pong:', self)

class C(A):
    def pong(self):
        print('PONG:', self)

class D(B, C):
    def ping(self):
        super().ping()
        print('post-ping:', self)

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)

d = D()
d.pong()
C.pong(d)

print(D.__mro__)
print(D.mro())

# Class and Instance Variables
class CountedObject:
    num_instances = 0

    def __init__(self):
        self.__class__.num_instances += 1
