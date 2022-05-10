import weakref
# Test weakref.ref(obj).proxy_class
#
# This is a test to demonstrate the use of weakref.ref(obj).proxy_class
# to get a proxy class for a given object.
#
# The proxy class can be used to create proxies for objects of the
# same type as obj.
#
# The proxy class is a subclass of weakref.ProxyType, which is a
# subclass of object.
#
# The proxy class has the same name as the class of the object,
# unless the object is an instance of a built-in type, in which case
# the name of the proxy class is the name of the built-in type.

# The proxy class has a __slots__ attribute, which is the same as the
# __slots__ attribute of the object's class, if any, or () otherwise.
#
# The proxy class has a __weakref__ slot, which is the same as the
# __weakref__ slot of the object's class, if any, or () otherwise.
#
# The proxy class has a __dict__ attribute, which is the same as the
# __dict__ attribute of the object
