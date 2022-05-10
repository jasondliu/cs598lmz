import ctypes
# Test ctypes.CField
mcv = ctypes.c_number.packed._test_var_
print(mcv)
# SampleField
# Test ctypes.CField.from_address()
mcadd = ctypes.CField.from_address(ctypes.c_number.packed, ctypes.c_number.packed)
print(mcadd)
# SampleField
# Test ctypes.CField.from_buffer()
mcfb = ctypes.CField.from_buffer(ctypes.c_number.packed, ctypes.c_number.packed)
print(mcfb)
# SampleField
# Test ctypes.CField.from_buffer_copy()
mcbfcp = ctypes.CField.from_buffer_copy(ctypes.c_number.packed, ctypes.c_number.packed)
print(mcbfcp)
# SampleField
# Test ctypes.CField.in_dll()
mcid = ctypes.CField.in_dll(ctypes.c_number.packed, ctypes.c_number.packed)
# SampleField
print(mcid)
# Test
