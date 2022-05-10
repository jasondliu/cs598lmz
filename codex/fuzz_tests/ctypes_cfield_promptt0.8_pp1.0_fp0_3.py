import ctypes
# Test ctypes.CField()

# Check that no argument fails
try:
    ctypes.CField()
except TypeError:
    pass
else:
    print("no TypeError")

# Check that only one integer fails
try:
    ctypes.CField(1, 2)
except TypeError:
    pass
else:
    print("no TypeError")

# Check that only one string fails
try:
    ctypes.CField('abc')
except TypeError:
    pass
else:
    print("no TypeError")

# Check that a simple definition works
cf = ctypes.CField(ctypes.c_int)
print(cf.offset, cf.type)

# Check that a string and an object works
cf = ctypes.CField('abc', ctypes.c_int)
print(cf.offset, cf.type)
