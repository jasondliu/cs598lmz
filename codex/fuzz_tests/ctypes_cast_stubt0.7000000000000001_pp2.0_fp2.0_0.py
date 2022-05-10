import ctypes
ctypes.cast(my_int, ctypes.c_void_p).value

def address(obj):
    print(ctypes.cast(obj, ctypes.c_void_p).value)

address(my_int)

# Dummy class to illustrate the point
class Dummy:
    pass

d = Dummy()

address(d)

# This is how to use the object identifier as a hash
hash(my_int)

# An object's identity never changes, but it's value can change
my_int = 500
print(id(my_int))

# Use is to check if two objects are the same
a = 10
b = 10
print(a is b)

# Use == to check if two objects are equal
a = 500
b = 500
print(a == b)

# This is how to check if two objects are the same
a = 500
b = 500
print(a is b)

# This is how to check if two objects are the same
a = 5.0
b = 5.0
print(a is b)

# This
