import ctypes
ctypes.cast(0xDEADBEEF, ctypes.c_void_p).value

# address
seg = ctypes.c_void_p.from_address(0xDEADBEEF)
seg.value

# l2 = ctypes.c_void_p.from_address(0x7ff7ae5f5c7c)
# seg.value - l2.value

# ctypes.c_int.from_address(0xDEADBEAD).value
# hex(0xDEADBEEF - 0x7ff7ae5f5c7c)


# ######################################################################################################################

# import ctypes
# ctypes.cast(0xDEADBEEF, ctypes.c_void_p).value
# # address
# seg = ctypes.c_void_p.from_address(0xDEADBEEF)
# seg.value
# l2 = ctypes.c_void_p.from_address(0x7ff7ae5f5c7c)
# seg.
