import weakref
# Test weakref.ref()

class MyClass:
    pass

def callback(ref):
    print('callback({!r})'.format(ref))

obj = MyClass()
r = weakref.ref(obj, callback)
print('obj:', obj)
print('ref:', r)
print('r():', r())
print('deleting obj')
del obj
print('r():', r())

# Test weakref.WeakKeyDictionary

class MyClass:
    pass

obj = MyClass()
d = weakref.WeakKeyDictionary()
d['primary'] = obj
print(d['primary'])
del obj
print(d.get('primary'))

# Test weakref.WeakValueDictionary

class MyClass:
    pass

obj = MyClass()
d = weakref.WeakValueDictionary()
d['primary'] = obj
print(d['primary'])
del obj
print(d.get('primary'))

# Test weakref.WeakSet

class MyClass:
    pass

obj = MyClass()
s = weakref
