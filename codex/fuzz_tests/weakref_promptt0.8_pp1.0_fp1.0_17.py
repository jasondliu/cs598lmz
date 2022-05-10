import weakref
# Test weakref.ref
a = weakref.ref('hello')
print(a())
print(type(a))
print(a())
b = a
print(b)
print(b())

a = weakref.ref('hello')
print(a)
print(a())
b = weakref.ref('hello')
print(b)
print(b())

# Test weakref.proxy
print()
print('Test weakref.proxy')
a = weakref.proxy('hello')
print(a)
print(type(a))
print(a)
b = a
print(b)
print(b)

a = weakref.proxy('hello')
print(a)
print(a)

# Test weakref.finalize
print()
print('Test weakref.finalize')

# Test weakref.getweakrefcount
print()
print('Test weakref.getweakrefcount')

# Test weakref.getweakrefs
print()
print('Test weakref.getweakrefs')

# Test weakref.WeakKeyDictionary
print()
print('
