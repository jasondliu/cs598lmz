import ctypes
ctypes.cast(results[0].get_data(), ctypes.POINTER(ctypes.c_float)).contents.value
