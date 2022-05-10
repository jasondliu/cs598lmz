import ctypes
# Test ctypes.CFUNCTYPE
func = ctypes.CFUNCTYPE(
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_float,
    ctypes.c_char
)(add)
print("Using CFUNCTYPE: {}".format(func(1, 2, 3, 4.0, "a")))

# Test ctypes.PYFUNCTYPE
func = ctypes.PYFUNCTYPE(
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_float,
    ctypes.c_char
)(add)
print("Using PYFUNCTYPE: {}".format(func(1, 2, 3, 4.0, "a")))
</code>
Note the only difference between the two examples is the use of CFUNCTYPE and PYFUNCTYPE. Any ideas on how I can fix this so I can use
