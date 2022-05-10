import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

class MyObject:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return "<MyObject: %r>" % self.name

obj = MyObject("test")
ref = weakref.ref(obj)

print("obj:", obj)
print("ref:", ref)
print("ref():", ref())

del obj
gc.collect()

print("ref:", ref)
print("ref():", ref())

obj = MyObject("new test")
print("obj:", obj)
print("ref():", ref())
