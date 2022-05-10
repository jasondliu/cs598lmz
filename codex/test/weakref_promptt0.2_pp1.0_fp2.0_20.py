import weakref
# Test weakref.ref() with a class instance.

class C:
    pass

o = C()
r = weakref.ref(o)

print(r())
print(r() is o)

o2 = C()
r2 = weakref.ref(o2)

print(r2())
print(r2() is o2)

print(r() is r2())

del o2
print(r2())

del o
print(r())

print(r() is None)
print(r() is None)

print(r2() is None)
print(r2() is None)

# Test weakref.ref() with a class instance and a __del__ method.

class D:
    def __del__(self):
        print("D.__del__")

o = D()
r = weakref.ref(o)

print(r())
print(r() is o)

o2 = D()
r2 = weakref.ref(o2)

print(r2())
