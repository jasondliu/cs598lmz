import weakref
# Test weakref.ref(func)

def foo():
    pass

wr = weakref.ref(foo)
print(wr)
print(wr())

# Test weakref.ref(object)

class Foo(object):
    pass

obj = Foo()
wr = weakref.ref(obj)
print(wr)
print(wr())
print(wr() is obj)

# Test weakref.WeakValueDictionary

d = weakref.WeakValueDictionary()
obj = Foo()
d["foo"] = obj
print(d["foo"] is obj)
print(len(d))
print(d.get("foo"))

del obj
print(d.get("foo"))
print(len(d))
