import ctypes
# Test ctypes.CFUNCTYPE()
def int_array_to_chr_array(int_array):
    return ''.join(map(chr, int_array))
python_callback = ctypes.CFUNCTYPE(int, ctypes.POINTER(ctypes.c_uint32))(int_array_to_chr_array)

CONVERT_TO_STRING = python_callback
def f_callback(dest):
    for i in range(0, 3):
        dest[i] = 55 + i

f_callback_prototype = ctypes.CFUNCTYPE(None, ctypes.POINTER(ctypes.c_uint32))
f_callback_pointer = ctypes.cast(f_callback, f_callback_prototype)
f_callback_pointer(ctypes.cast(ctypes.c_uint32(4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
