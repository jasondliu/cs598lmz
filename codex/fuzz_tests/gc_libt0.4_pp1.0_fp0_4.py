import gc, weakref

class WeakKeyDictionary(object):
    def __init__(self):
        self.d = weakref.WeakKeyDictionary()
    def __setitem__(self, key, value):
        self.d[key] = value
    def __getitem__(self, key):
        return self.d[key]

class MyClass(object):
    pass

d = WeakKeyDictionary()
m1 = MyClass()
m2 = MyClass()
d[m1] = 1
d[m2] = 2
print(d[m1])
print(d[m2])

del m1
gc.collect()
print(d[m2])

del m2
gc.collect()
print(d[m2])
</code>

