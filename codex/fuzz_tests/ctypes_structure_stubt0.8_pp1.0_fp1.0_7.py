import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long(17)
    y = ctypes.c_long(19)

s = S()

# Setter function
def s_set(obj, val):
    print("s.setter(%s)" % (val, ))
    obj.x = val

# Getter function
def s_get(obj):
    print("s.getter()")
    return obj.x

# Make a property object
s_prop = property(s_get, s_set)

# Make a property descriptor
s_descr = property(s_get, s_set)

# Bind the property to the class
S.s = s_descr

# Test the property
print("s.s =", s.s)
print("s.s = 21")
print("s.s =", s.s)
