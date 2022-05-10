import weakref
# Test weakref.ref()

class C:
    def __init__(self):
        self.x = 1

c = C()
r = weakref.ref(c)
print(r(), r() is c)

c.x = 2
print(r(), r().x)

del c
print(r())

a = []
r = weakref.ref(a)
print(r(), r() is a)

a.append(1)
print(r(), r()[0])

del a
print(r())

class C:
    def __init__(self):
        self.x = 1

c = C()
r = weakref.ref(c)
print(r(), r() is c)

c.x = 2
print(r(), r().x)

del c
print(r())

a = []
r = weakref.ref(a)
print(r(), r() is a)

a.append(1)
print(r(), r()[0])

del a
print(r())

# Test weakref
