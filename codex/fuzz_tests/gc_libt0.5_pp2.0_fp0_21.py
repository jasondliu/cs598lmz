import gc, weakref, sys

class A:
    pass
a = A()
print(a)

del a
print(gc.collect())

print()

class B:
    def __del__(self):
        print('B.__del__')

b = B()
w = weakref.ref(b)
print(w)
print(w())

del b
print(gc.collect())
print(w)
print(w())

print()

class C:
    def __del__(self):
        print('C.__del__')

c = C()
w = weakref.ref(c)
print(w)
print(w())

del c
print(gc.collect())
print(w)
print(w())

print()

class D:
    def __del__(self):
        print('D.__del__')

d = D()
w = weakref.ref(d)
print(w)
print(w())

del d
print(gc.collect())
print(w)
print(w
