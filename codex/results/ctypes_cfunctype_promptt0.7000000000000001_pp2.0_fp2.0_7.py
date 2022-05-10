import ctypes
# Test ctypes.CFUNCTYPE()
# This function matches the prototype of the function we want
# to wrap.
def u_strlen(u):
    return len(u)

# Now we define a pointer to the above function
u_strlen_ptr = ctypes.CFUNCTYPE(ctypes.c_ulong, ctypes.c_wchar_p)(u_strlen)

# Now we can assign it to the libucd
libucd.ucd_get_property_value_name.argtypes = [ctypes.c_void_p, ctypes.c_ulong, ctypes.c_ulong, ctypes.c_wchar_p]
libucd.ucd_get_property_value_name.restype = ctypes.c_wchar_p

# Now we can use it
x = libucd.ucd_get_property_value_name(p_pvn, libucd.ucd_get_property_id_by_name(p_pvn, b"Line_Break"), libucd.ucd_get_property_value
