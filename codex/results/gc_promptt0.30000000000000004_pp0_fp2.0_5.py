import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'A(%r)' % self.name

def f():
    a = A('a')
    b = A('b')
    a.b = b
    b.a = a
    del a
    del b

print(gc.collect())
f()
print(gc.collect())
