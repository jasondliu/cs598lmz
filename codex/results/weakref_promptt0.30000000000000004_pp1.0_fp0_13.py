import weakref
# Test weakref.ref() with a class instance.
import weakref

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())
print(o)
o2 = r()
print(o is o2)
print(o == o2)
print(r == o2)
print(r is o2)
print(r() is o2)
print(r() == o2)
print(r() is o)
print(r() == o)

# Test weakref.ref() with a class instance and a callback.
import weakref

class C:
    pass

o = C()
l = []
r = weakref.ref(o, l.append)
print(r)
print(r())
print(o)
o2 = r()
print(o is o2)
print(o == o2)
print(r == o2)
print(r is o2)
print(r() is o2)
print(r() == o2)
print(r() is o)
print
