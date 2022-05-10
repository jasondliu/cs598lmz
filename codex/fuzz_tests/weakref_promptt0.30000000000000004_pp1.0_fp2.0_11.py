import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())

o2 = C()
r2 = weakref.ref(o2, lambda x: print("dead"))
print(r2)
print(r2())

del o2
print(r2())

# Test weakref.proxy()

class D:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

o = D(10)
p = weakref.proxy(o)
print(p)
print(p.value)

o2 = D(20)
p2 = weakref.proxy(o2, lambda x: print("dead"))
print(p2)
print(p2.value)

del o2
print(p2.value)
