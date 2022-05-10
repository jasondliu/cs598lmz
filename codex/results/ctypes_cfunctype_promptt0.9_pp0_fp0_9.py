import ctypes
# Test ctypes.CFUNCTYPE
CFUNCTYPE(c_int)(lambda arg1, arg2: arg1 + arg2)(3, 4)

try:
    ctypes.string_at(0)
except ValueError:
    print("ValueError")

try:
    ctypes.string_at(1)
except TypeError:
    print("TypeError")

def callback(int_arg, uint_arg, int_arg_p, uint_arg_p, l_arg, l_arg_p, p_arg,
             p_arg_p, void_arg_p, func_arg_p):
    return int_arg_p[0] + uint_arg_p[0] + l_arg_p[0] + p_arg_p[0]

callback_ptr = CFUNCTYPE(c_int, c_int, c_uint, POINTER(c_int), POINTER(c_uint),
                         POINTER(c_long), POINTER(c_long), POINTER(c_void_p),
                         POINTER(c_void_p), POINTER
