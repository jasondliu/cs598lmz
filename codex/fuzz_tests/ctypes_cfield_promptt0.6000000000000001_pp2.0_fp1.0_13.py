import ctypes
# Test ctypes.CField()

# Try to create a field without an offset
try:
    ctypes.CField()
except TypeError:
    print("passed")
else:
    print("failed")

# Create a field with an offset
field = ctypes.CField(ctypes.c_int, "offset")

# Check that the offset is set
if field.offset == "offset":
    print("passed")
else:
    print("failed")

# Check that the offset is read-only
try:
    field.offset = 42
except AttributeError:
    print("passed")
else:
    print("failed")

# Try to create a field with a bad offset
try:
    ctypes.CField(ctypes.c_int, "bad-offset")
except ValueError:
    print("passed")
else:
    print("failed")

# Try to create a field with a bad offset
try:
    ctypes.CField(ctypes.c_int, 42)
except TypeError:
    print("passed")
else:
    print("
