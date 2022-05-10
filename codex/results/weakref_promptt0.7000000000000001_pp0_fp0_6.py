import weakref
# Test weakref.ref()

class MyBase:
    pass

class MyClass(MyBase):
    pass

def callback(obj):
    print('callback({})'.format(obj))

obj = MyClass()
check = weakref.ref(obj, callback)

print('obj:', obj)
print('check:', check)
print('obj is check:', obj is check)

print()
print('deleting obj')
del obj
print('check:', check)
# Test weakref.WeakSet

class MyBase:
    pass

class MyClass(MyBase):
    pass

obj = MyClass()

s = weakref.WeakSet()
s.add(obj)

print('obj:', obj)
print('s:', s)
print('obj in s:', obj in s)

print()
print('deleting obj')
del obj
print('obj in s:', obj in s)
print('s:', s)
# Test weakref.WeakValueDictionary

class MyBase:
    pass

class MyClass(My
