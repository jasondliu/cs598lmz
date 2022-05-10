import ctypes
# Test ctypes.CFUNCTYPE(None, ctypes.c_int), i.e. do not pass a pointer
user_callback_one = ctypes.CFUNCTYPE(None, ctypes.c_int)(lambda x: None)
try:
    lib.do_something_with_callback_pint(user_callback_one)
except ValueError as e:
    print("passed user_callback_one", e)

# Test ctypes.CFUNCTYPE(..., ctypes.POINTER(ctypes.c_int)), i.e. pass a pointer
user_callback_two = ctypes.CFUNCTYPE(None, ctypes.POINTER(ctypes.c_int))(lambda x: None)
try:
    lib.do_something_with_callback_pint(user_callback_two)
except ValueError as e:
    print("passed user_callback_two", e)

# Test ctypes.CFUNCTYPE(None, ctypes.c_int), i.e. do not pass a pointer
user_callback_three = ctypes.CFUNCT
