import weakref
# Test weakref.ref() with callable objects.

# Create a callable object.
class C:
    def __call__(self):
        pass

# Create a weak reference to the callable object.
c = C()
r = weakref.ref(c)

# The weak reference should be callable.
r()

# The weak reference should be usable as a weakref.proxy.
p = weakref.proxy(c)
p()

# The weak reference should be usable as a weakref.proxy_factory.
p = weakref.proxy_factory(c)
p()

# The weak reference should be usable as a weakref.proxy_factory.
p = weakref.proxy_factory(c)
p()

# The weak reference should be usable as a weakref.proxy_factory.
p = weakref.proxy_factory(c)
