import weakref
# Test weakref.ref(x) with a class that has a __del__ method.
# The weakref should not call the __del__ method.

class Foo:
    def __init__(self, x):
        self.x = x
    def __del__(self):
        print("Deleting %s" % self.x)

def callback(r):
    print("Callback called with", r)

f = Foo(10)
r = weakref.ref(f, callback)
print("Created weak reference", r)

print("Deleting f")
del f
print("Calling gc.collect()")
gc.collect()
print("Callback should not have been called")
