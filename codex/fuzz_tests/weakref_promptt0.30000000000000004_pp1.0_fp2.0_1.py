import weakref
# Test weakref.ref(obj)

class MyClass:
    pass

obj = MyClass()
r = weakref.ref(obj)
print(r)

print(r())

obj = None
print(r())

# Test weakref.ref(obj, callback)

class MyClass:
    pass

obj = MyClass()
r = weakref.ref(obj, lambda x: print('callback'))
print(r)

print(r())

obj = None
print(r())

# Test weakref.WeakKeyDictionary

class MyClass:
    pass

obj1 = MyClass()
obj2 = MyClass()
obj3 = MyClass()

d = weakref.WeakKeyDictionary()
d[obj1] = 1
d[obj2] = 2
d[obj3] = 3

print(d)

obj1 = None
print(d)

obj2 = None
print(d)

obj3 = None
print(d)

# Test weakref.WeakValueDictionary

class MyClass:
    pass
