from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('h')
s.pack(1)

# Descriptor
class C:
    def __get__(self, instance, owner):
        print('get')
        return self

    def __set__(self, instance, value):
        print('set')

class D:
    x = C()

d = D()
d.x = 1
d.x

# Iterator
class Fib:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib

for n in Fib(1000):
    print(n, end=' ')

# Generator
def fib(max):
    a, b = 0, 1
    while a < max:
        yield a

