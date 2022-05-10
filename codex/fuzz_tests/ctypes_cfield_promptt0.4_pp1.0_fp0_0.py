import ctypes
# Test ctypes.CField

# This is a simple test to see if the CField object is working.  The
# CField object is a wrapper around a ctypes data type.  It is used
# to create a field in a C structure.

# This test creates a CField that contains a ctypes.c_int.  It then
# creates a CStructure that contains a single field that is a CField.
# The CField is initialized with the value 10.  The CStructure is then
# printed to show the value of the CField.

# CField is not intended to be used directly.  It is used by the
# CStructure class to create C structures.

# Create a CField that contains a c_int
cField = CField(ctypes.c_int)

# Create a CStructure that contains a single field that is a CField
cStruct = CStructure(fields=[cField])

# Initialize the CField to 10
cStruct.field = 10

# Print the CStructure
print(cStruct)
