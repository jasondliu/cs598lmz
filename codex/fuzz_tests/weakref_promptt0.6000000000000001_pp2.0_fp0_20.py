import weakref
# Test weakref.ref(c)
# Test weakref.proxied_type(r)
# Test weakref.proxy(r)
# Test weakref.getweakrefcount(c)
# Test weakref.getweakrefs(c)

# Test function to return weakrefable objects
def make_object(x):
    class A(object):
        pass
    return A()

# Test function to take a weakrefable object
def take_object(x):
    pass

# Test function to return a weak reference
def make_weakref(x):
    return weakref.ref(x)

# Test function to take a weak reference
def take_weakref(x):
    pass

# Test function to return a proxy
def make_proxy(x):
    return weakref.proxy(x)

# Test function to take a proxy
def take_proxy(x):
    pass

# Test function to return a proxied type
def make_proxied_type(x):
    return weakref.proxied_type(x)

# Test function to take a proxied
