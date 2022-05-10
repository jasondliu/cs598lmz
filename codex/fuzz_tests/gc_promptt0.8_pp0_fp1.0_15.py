import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() is triggered on __del__
class A(object):
    def __del__(self):
        gc.collect()

# Create a reference cycle
a = A()
a.b = a

# Break the cycle
a = None

# Create the same reference cycle
a = A()
a.b = a

# Assign the same weak reference to a different object
b = A()
b.b = b

a.b = b
# Create the same reference cycle
a = A()
a.b = a

# Assign the same weak reference to a different object
b = A()
b.b = b

a.b = b
b = None
# Create the same reference cycle
a = A()
a.b = a

# Assign the same weak reference to a different object
b = A()
b.b = b

a.b = b
b = None
gc.collect()
for o in gc.get_objects():
    try:
        if weakref.getweakrefs(o):
            print o
    except:

