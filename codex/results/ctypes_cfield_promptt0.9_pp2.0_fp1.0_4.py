import ctypes
# Test ctypes.CField
#
# ctypes.CField is a C-style 'union' factory. It is a class decorator, the
# class is the 'union'. It takes a list of name-type pairs, the class
# attributes will be set to field objects created from them.
#
# The field objects act like the ordinary type objects, they are callable,
# and return class instances, just like the types do.
#
# The instances will be subclasses of the class, and have members
# 'value', plus the name attributes from the field list. These members
# reference the same memory.
#
# The field objects can be used to set the value of the class
# instances.
#
# The fields always return native case, the field object
# constructor can specialize this default (the default of the default
# is the same as the native case of the field type).

# The field objects also support from_address() and from_param()
# methods. from_address() needs a ctypes instance, returns a new
# instance of the CField assigned to that address.
#
# from_param() also takes an instance of ctypes,
