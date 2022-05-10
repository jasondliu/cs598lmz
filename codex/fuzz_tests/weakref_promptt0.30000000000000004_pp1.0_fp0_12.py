import weakref
# Test weakref.ref(obj) and weakref.proxy(obj)

class Foo:
    pass

class Bar:
    pass

f = Foo()
b = Bar()

fwr = weakref.ref(f)
bwr = weakref.ref(b)

fwpr = weakref.proxy(f)
bwpr = weakref.proxy(b)

print(fwr())
print(bwr())

print(fwpr)
print(bwpr)

print(type(fwr))
print(type(bwr))

print(type(fwpr))
print(type(bwpr))

print(fwr is fwpr)
print(bwr is bwpr)

print(fwr() is fwpr)
print(bwr() is bwpr)

print(fwr() is f)
print(bwr() is b)

print(fwpr is f)
print(bwpr is b)

del f
del b

print(fwr())
print(bwr())

print(fwpr)
