import weakref
# Test weakref.ref() and weakref.proxy()
#
# weakref.ref(object[, callback])
# weakref.proxy(object[, callback])
#
# Create a weak reference or a weak reference proxy for an object.
#
# A weak reference is simply a reference to an object that does not prevent
# the object from being garbage collected.  When the object is garbage
# collected, the weak reference is automatically removed.  The object is
# said to be weakly referenced.
#
# A weak reference proxy is a weak reference that is callable.  When called,
# the proxy redirects the call to the object.  If the object has been
# garbage collected, calling the proxy will cause a ReferenceError to be
# raised.
#
# The callback, if given, is called with the weak reference as its only
# argument when the referenced object is about to be finalized; that is,
# just before its reference count drops to zero.  The callback is called
# from the garbage collector's thread, and not the thread that is
# deallocating the object.  The callback should be a callable Python object.
#
# If
