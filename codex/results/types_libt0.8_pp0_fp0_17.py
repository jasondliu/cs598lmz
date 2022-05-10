import types
types.new_class("TheType", (int,), {}) == TheType

# While __metaclass__ checks look for a metaclass in the class dict,
# it also checks for a metaclass in the base list.
# The base list is checked in the same order as for MRO calculation.
# Here is an example:
#
#   class M1(type):
#       def foo(self): return 1
#
#   class M2(type):
#       def foo(self): return 2
#
#   class X(object):
#       __metaclass__ = M1
#
#   class Y(X):
#       __metaclass__ = M2
#
#   class Z(Y):
#       pass
#
#   # This will make a type with M1 as its metaclass:
#   class A(object, X):
#       pass
#
#   # This will make a type with M2 as its metaclass:
#   class B(object, Z):
#       pass

# Note that this is the exact reverse of the order
