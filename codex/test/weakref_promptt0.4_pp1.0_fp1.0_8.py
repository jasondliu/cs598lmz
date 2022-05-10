import weakref
# Test weakref.ref(obj)
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)
d = weakref.ref(a)
print(d)
print(d())
print(a)

# Test weakref.ref(obj, callback)
def callback(x):
    print('callback', x)

a = A(10)
d = weakref.ref(a, callback)
print(d)
print(d())
print(a)

del a
print(d())

# Test weakref.WeakKeyDictionary
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

d = weakref.WeakKeyDictionary()
a = A(10)
d[a] = 'something'
print(d[a])
print(d)

del a
print(d)

# Test weakref
