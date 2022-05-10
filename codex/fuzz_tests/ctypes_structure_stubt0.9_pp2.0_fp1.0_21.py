import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(5)
    y = ctypes.c_int(6)

def print_fields(name, typ):
    print "Fields of %s" % name
    if typ._fields_ is None:
        print "\t(Field-less structure)"
    else:
        for fname, ftype in typ._fields_:
            print "\t%s" % fname
    print

print_fields("Structure", ctypes.Structure)
print_fields("S", S)

# Attributes are stored by name in the Field class
assert hasattr(S, "y"), "S has no attribute 'y'"
del S.y
assert S._fields_ == (("x", ctypes.c_int)), "S._fields_ should contain one element"

# Add a new attribute
S.z = ctypes.c_int
assert S._fields_ == (("x", ctypes.c_int), ("z", ctypes.c_int)), "S._fields_ should contain two elements"

# these raises TypeErrors:
try:
   
