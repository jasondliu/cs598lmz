import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    def __init__(self, x):
        self.x = x
    def __del__(self):
        print("__del__ called on", self.x)

class Bar(Foo):
    def __del__(self):
        print("Bar's __del__ called")
        Foo.__del__(self)

foo = Foo(1)
bar = Bar(2)

# Some other objects:
b = [1.5]
c = 'x' * 1000
d = {'x': 1, 'y': 2}

# The weakref callback
def callback(r):
    print("weakref callback called on", r)

a = weakref.ref(foo, callback)
e = weakref.ref(bar, callback)

# Check that the weakrefs work
print(a(), a() is foo)
print(e(), e() is bar)

# Clear all references
del foo, bar

# Collect
print("Collecting...")
n = gc.collect()
print("Unreachable objects:
