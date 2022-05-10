import types
types.ModuleType

# Eigenschaften der Datentypen
#---------------------------------------------------------------------
# https://docs.python.org/3/library/stdtypes.html#data-model
#---------------------------------------------------------------------

# isinstance:--------
#---------------------------------------------------------------------
isinstance("a", str)  # True
isinstance("a", int)  # False

a = "a"
isinstance(a, str)   # True
isinstance(a, object)# True

a = ""
isinstance("", int)  # False
isinstance("", object)# True

# issubclass:--------
#---------------------------------------------------------------------
class A():
	pass

class B(A):
	pass
issubclass(A, object)   # True
issubclass(B, object)   # True
issubclass(B, A)   # True
issubclass(A, B)   # False

# is:--------
#---------------------------------------------------------------------
a = "a"
b = a
c = "a"
d = "a"
e = d
