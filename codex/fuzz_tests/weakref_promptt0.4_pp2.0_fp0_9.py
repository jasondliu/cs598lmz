import weakref
# Test weakref.ref(f)

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)
d = weakref.WeakKeyDictionary()
d[a] = 1
print(d[a])
del a
print(d.data)

# Test weakref.ref(f, callback)

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)
d = weakref.WeakKeyDictionary()
d[a] = 1
print(d[a])
r = weakref.ref(a, lambda x: print('deleted', x))
del a
print(d.data)

# Test weakref.proxy(f)

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(
