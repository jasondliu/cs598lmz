import ctypes
# Test ctypes.CField

# Get the address of a global variable
globvar = 91
globvar_address = ctypes.addressof(globvar)

# Define a ctypes structure
class Test(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_char * 4),
                ('c', ctypes.CField)]

# Create an instance of the structure, and set its c field
# to point at the global variable.
test = Test()
test.c = ctypes.cast(globvar_address, ctypes.c_void_p)
print(test.c.value)

# Write to the memory referenced by the c field
ctypes.cast(test.c, ctypes.POINTER(ctypes.c_int))[0] = 999
print(globvar)
