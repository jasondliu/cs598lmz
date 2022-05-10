import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

# A test class to make sure that instance dictionaries are
# collected.
class C:
    def __init__(self):
        self.__dict__

# Create a reference cycle
a = C()
a.x = a
del a
# Create an instance with a __del__ method.
class C(object):
    def __del__(self):
        pass

# Create a reference cycle
a = C()
a.x = a
del a
# Create a reference cycle
a = []
a.append(a)
del a
# Create a large object with a finalizer.
class C(object):
    def __del__(self):
        pass

a = C()
a.x = a
a.y = [a]
del a
gc.collect()
# Create a large object with a finalizer.
class C(object):
    def __del__(self):
        pass

a = C()
a.x = a
a.y = [a]
del a
gc.collect()
# Create a large object with a finalizer
