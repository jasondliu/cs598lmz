import weakref
# Test weakref.ref(func)
def func(i):
    return i

wr = weakref.ref(func)

print(wr)
print(wr())
print(wr() is func)

# Test weakref.ref(lambda: None)
wr = weakref.ref(lambda: None)
print(wr)
print(wr() is None)

# Test weakref.ref(class)
class Foo:
    pass

wr = weakref.ref(Foo)
print(wr)
print(wr() is Foo)

# Test weakref.ref(instance)
class Foo:
    pass

wr = weakref.ref(Foo())
print(wr)
print(wr() is None)

# Test weakref.ref(list)
lst = []
wr = weakref.ref(lst)
print(wr)
print(wr() is lst)

# Test weakref.ref(dict)
dct = {}
wr = weakref.ref(dct)
print(wr)
print(wr() is dct)

# Test weakref
