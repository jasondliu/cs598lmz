import weakref
# Test weakref.ref() and weakref.proxy()

class A:
    pass

a = A()
a.x = 10

r = weakref.ref(a)
p = weakref.proxy(a)

print(r(), p.x)
del a
print(r(), p.x)
