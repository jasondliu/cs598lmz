import ctypes
ctypes.cast(1, ctypes.c_ulonglong)

# test_ctypes_c_ulonglong_to_python.py:3: RuntimeWarning: overflow encountered in long_scalars

# -2**64 + 2**64 - 2
ctypes.cast(-18446744073709551614, ctypes.c_ulonglong)

# test_ctypes_c_ulonglong_to_python.py:6: RuntimeWarning: overflow encountered in long_scalars

# -2**64 + 2**64 - 1
ctypes.cast(-18446744073709551615, ctypes.c_ulonglong)

# test_ctypes_c_ulonglong_to_python.py:9: RuntimeWarning: overflow encountered in long_scalars

# -2**64 + 2**64 - 0
ctypes.cast(-18446744073709551616, ctypes.c_ulonglong)

# test_ctypes_c_ulonglong_to_python.py:12: RuntimeWarning: overflow encountered in long_sc
