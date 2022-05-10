import weakref
# Test weakref.ref(object)

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())

o2 = C()
r2 = weakref.ref(o2, lambda x: print('callback'))
print(r2)
print(r2())

del o2
print(r2())

o = C()
r = weakref.ref(o)
print(r)
print(r())

o2 = C()
r2 = weakref.ref(o2, lambda x: print('callback'))
print(r2)
print(r2())

del o2
print(r2())

# Test weakref.ref(object, callback)

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())

o2 = C()
r2 = weakref.ref(o2, lambda x: print('callback'))
print(r2)
print(r2())

del o2

