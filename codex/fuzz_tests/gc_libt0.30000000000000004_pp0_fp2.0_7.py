import gc, weakref

class WeakKeyDictionary:
    def __init__(self):
        self.d = weakref.WeakKeyDictionary()
    def __setitem__(self, key, value):
        self.d[key] = value
    def __getitem__(self, key):
        return self.d[key]

class C:
    pass

c1 = C()
c2 = C()
c3 = C()

d = WeakKeyDictionary()
d[c1] = 1
d[c2] = 2

print(d[c1])
print(d[c2])

del c1
del c2

gc.collect()

print(d[c3])
