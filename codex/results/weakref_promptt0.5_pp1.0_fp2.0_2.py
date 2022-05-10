import weakref
# Test weakref.ref
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
print(d['primary'])
del a
print(d['primary'])

# Test weakref.proxy
class B:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

b = B(10)
p = weakref.proxy(b)
print(p)
del b
print(p)
