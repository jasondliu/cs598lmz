import ctypes
ctypes.cast(GET_BAG()[0].operands[0], ctypes.POINTER(ctypes.c_void_p)).contents.value
# ctypes.cast(GET_BAG()[0].operands[1], ctypes.POINTER(ctypes.c_void_p)).contents.value

# sconv = ctypes.cast(s, ctypes.c_void_p).value
# dconv = ctypes.cast(d, ctypes.c_void_p).value
# print("debug_0")
# print(ctypes.cast(out, ctypes.c_void_p).value)

# dtype.save(ctypes.cast(s, ctypes.c_void_p).value, 1000)
# print(dtype.load(1001))
# dtype.save(ctypes.cast(d, ctypes.c_void_p).value, 2000)
# print(dtype.load(2001))
# d.store(2001)

# print(ctypes.addressof(ast.DebugAssignment(
#     ast.
