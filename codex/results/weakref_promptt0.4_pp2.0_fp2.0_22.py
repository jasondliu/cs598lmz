import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)

print(r())
print(r() is o)

o2 = r()
print(o2 is o)

del o
print(r())

del o2
print(r())

r = weakref.ref(1)
print(r())
print(r() is 1)

r = weakref.ref(1.0)
print(r())
print(r() is 1.0)

r = weakref.ref(None)
print(r())
print(r() is None)

r = weakref.ref(True)
print(r())
print(r() is True)

r = weakref.ref(False)
print(r())
print(r() is False)

r = weakref.ref(Ellipsis)
print(r())
print(r() is Ellipsis)

r = weakref.ref(NotImplemented)
print(r())
print(r() is NotImplemented)
