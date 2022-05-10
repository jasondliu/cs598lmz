import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)
    y = ctypes.c_int(2)
    z = ctypes.c_int(3)

s1 = S()
s2 = S()

# Accessing the attributes via the instance attribute
print(s1.x, s1.y, s1.z)

# Accessing the attributes via the fields dictionary attribute
for attr in s1._fields_:
    print('{}: {}'.format(attr, s1.__getattribute__(attr)))

# Accessing the attributes via the _asdict() method
for attr,val in s1._asdict().items():
    print('{}: {}'.format(attr, val))

# Accessing the attributes via attribute pointers
for attr in s1._fields_:
    attr_ptr = getattr(s1, attr)
    print('{}: {}'.format(attr, attr_ptr.value))

# If we change the value of on of the attributes in s2, and assign it to s1
s2.x = 10
s1 =
