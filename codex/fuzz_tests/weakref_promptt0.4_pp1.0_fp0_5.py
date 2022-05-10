import weakref
# Test weakref.ref() with a class instance.

class MyClass:
    pass

def callback(r):
    print('callback(', r, ')')

obj = MyClass()
r = weakref.ref(obj, callback)
print('obj:', obj)
print('r:', r)
print('r():', r())
print('deleting obj')
del obj
print('r():', r())
print('r:', r)
