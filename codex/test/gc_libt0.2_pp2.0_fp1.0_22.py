import gc, weakref

class C:
    pass

o = C()
r = weakref.ref(o)

print(r)
print(r())

o2 = C()
r2 = weakref.ref(o2)

print(r2)
print(r2())

print(r is r2)
print(r() is r2())

print(r() is o)
print(r2() is o2)

print(r() is o2)
print(r2() is o)

print(r() == o)
print(r2() == o2)

print(r() == o2)
print(r2() == o)

print(r == o)
print(r2 == o2)

print(r == o2)
print(r2 == o)

print(r == 42)
print(r2 == 42)

print(42 == r)
print(42 == r2)

print(r == None)
print(r2 == None)

print(None == r)
