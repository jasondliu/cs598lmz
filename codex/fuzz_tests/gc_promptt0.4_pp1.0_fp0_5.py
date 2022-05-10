import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class C:
    pass

# Create a cycle
x = C()
x.a = x
del x

# Create a reachable object
y = C()

# Enter some reference cycles
for i in range(10):
    x = C()
    x.a = C()
    x.a.a = x

# Create a reachable object with a __del__ method
class D:
    def __del__(self):
        print('D.__del__')

d = D()

# Create some uncollectable objects
class E:
    def __del__(self):
        print('E.__del__')
        # Create a reference cycle
        self.a = []
        self.a.append(self)

e = E()

# Create some objects with finalizers
class F:
    def __del__(self):
        print('F.__del__')

f = F()
w = weakref.ref(f)

# Create some uncollectable objects with finalizers
class G:
    def __del__
