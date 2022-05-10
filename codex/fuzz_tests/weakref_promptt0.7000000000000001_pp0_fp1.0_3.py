import weakref
# Test weakref.ref()
class Foo:
    pass

f = Foo()
r = weakref.ref(f)

# Outputs <weakref at 0x1005547b8; to 'Foo' at 0x100535198>
print(r)

# Outputs <class '__main__.Foo'>
print(r().__class__)

# Outputs True
print(r() is f)

# Outputs True
print(r() == f)

# Outputs False
print(r() is None)

# Outputs True
print(r() == None)
# Test weakref.WeakValueDictionary()
class Foo:
    pass

f = Foo()

d = weakref.WeakValueDictionary()
d['foo'] = f

# Outputs <weakref at 0x1005547b8; to 'Foo' at 0x100535198>
print(d['foo'])

# Outputs <class '__main__.Foo'>
print(d['foo'].__class__)

# Outputs True
print(d
