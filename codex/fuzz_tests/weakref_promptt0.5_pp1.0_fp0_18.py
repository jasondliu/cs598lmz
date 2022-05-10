import weakref
# Test weakref.ref(c) and weakref.proxy(c)
class C:
    pass

c = C()
r = weakref.ref(c)
p = weakref.proxy(c)
print(r(), p)

del c
print(r(), p)

# Test weakref.ref(c) and weakref.proxy(c)
class C:
    pass

c = C()
r = weakref.ref(c)
p = weakref.proxy(c)
print(r(), p)

del c
print(r(), p)
