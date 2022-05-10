import ctypes
ctypes.cast(labs, ctypes.POINTER(ctypes.c_char_p))
ctypes.cast(labs, ctypes.POINTER(ctypes.c_char_p))[0]
ctypes.cast(labs, ctypes.POINTER(ctypes.c_char_p))[0].value
ctypes.cast(labs, ctypes.POINTER(ctypes.c_char_p))[0].value.decode()
ctypes.cast(labs, ctypes.POINTER(ctypes.c_char_p))[1]
ctypes.cast(labs, ctypes.POINTER(ctypes.c_char_p))[1].value
ctypes.cast(labs, ctypes.POINTER(ctypes.c_char_p))[1].value.decode()
def split_std_string_p(string_p, string_count):
    values = []
    chars = string_p.value.decode()
    for i in range(string_count.value):
        values.append(chars[i*4:(i
