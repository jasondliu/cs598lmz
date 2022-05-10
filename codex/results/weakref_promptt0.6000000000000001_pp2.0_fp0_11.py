import weakref
# Test weakref.ref() and weakref.proxy()
# The weakref.ref() and weakref.proxy() functions create weak references and weak proxies to objects.
# A weak reference to an object is not enough to keep the object alive: when the only remaining references to a referent are weak references, garbage collection is free to destroy the referent and reuse its memory for something else.
# A weak reference to an object is a piece of metadata about the object that does not keep it alive.
# When an object is garbage collected, weak references to it are notified.
# To create a weak reference, use the weakref.ref() function.
# The result is an object that supports the same interface as the proxy type, but if called it returns None instead of raising ReferenceError.
# The referent may still be alive, in which case calling the reference is equivalent to calling the proxy.
# If the referent is no longer alive, calling the reference returns None.
# To create a weak proxy, pass the weak reference to the weakref.proxy() function.
# The result is an object that supports the same interface as the object that the reference was created from, but if called it raises ReferenceError instead of
