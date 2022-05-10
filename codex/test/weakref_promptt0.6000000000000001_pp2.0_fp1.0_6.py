import weakref
# Test weakref.ref(), weakref.proxy(), weakref.getweakrefcount() and
# weakref.getweakrefs()

class A:
    pass

a = A()
b = A()

wr = weakref.ref(a)
assert wr() is a

wp = weakref.proxy(a)
assert wp is a

assert weakref.getweakrefcount(a) == 1
assert weakref.getweakrefcount(b) == 0

assert weakref.getweakrefs(a) == [wr]
assert weakref.getweakrefs(b) == []

del a
assert wr() is None

try:
    wp.attribute
except ReferenceError:
    pass
else:
    print("wp.attribute didn't raise ReferenceError")

class C:
    pass

c = C()
wr = weakref.ref(c)

assert weakref.getweakrefs(c) == [wr]

try:
    del c.attribute
except AttributeError:
    pass
