import weakref
# Test weakref.ref(obj)
# Test weakref.proxy(obj)
# Test weakref.getweakrefcount(obj)
# Test weakref.getweakrefs(obj)
# Test weakref.ref(obj, callback)
# Test weakref.proxy(obj, callback)

# Weak references to objects can be created using the weakref.ref() function.
#
# The callback function is called when the reference object is about to be garbage collected.
#
# The weak references can only be used to access objects, not to call methods on them or access their attributes.

# A proxy is a weak reference that also provides access to attributes and methods of the referent.
#
# The proxy is created using the weakref.proxy() function.
#
# The weak reference object keeps a reference to the proxy.
#
# When the referent is garbage collected, the weak reference object is also garbage collected,
# and the proxy object becomes invalid.

# The number of weak references to an object can be obtained using the weakref.getweakrefcount() function.
#
# The list of weak reference objects can be obtained using the wea
