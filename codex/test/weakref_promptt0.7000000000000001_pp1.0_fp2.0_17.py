import weakref
# Test weakref.ref

class C:
    pass

c = C()

print('callable(C):', callable(C))
print('callable(c):', callable(c))

print('weakref.ref(C):', weakref.ref(C))
print('weakref.ref(C)():', weakref.ref(C)())
print('weakref.ref(c):', weakref.ref(c))
print('weakref.ref(c)() is c:', weakref.ref(c)() is c)

print('weakref.proxy(C):', weakref.proxy(C))
print('weakref.proxy(C)() is C:', weakref.proxy(C)() is C)
print('weakref.proxy(c) is c:', weakref.proxy(c) is c)

# Test weakref.proxy on class

class D:
    def __init__(self, x):
        self.x = x

d = D(42)
p = weakref.proxy(d)

