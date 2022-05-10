import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int),
        # this is a CField
        ('array', ctypes.c_int * 4)
    ]

x = X()
x.x = 1
x.y = 2
x.array[0] = 10
x.array[1] = 20
x.array[2] = 30
x.array[3] = 40

# Test ctypes.CField.from_address
# Get the address of the third element of the array
addr = ctypes.addressof(x.array)
addr += 2 * ctypes.sizeof(ctypes.c_int)

# Cast the address to a pointer to an int
ptr = ctypes.c_int.from_address(addr)
ptr.value = 300

# Test ctypes.CField.from_buffer
ptr = ctypes.c_int.from_buffer(x.array, 4)
ptr.value = 400

# Test ctypes
