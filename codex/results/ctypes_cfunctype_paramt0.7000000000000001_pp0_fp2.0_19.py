import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# get the function
lib = ctypes.CDLL("./liblazy_string.so")
lib.lazy_string_at = FUNTYPE(lib.lazy_string_at)
lib.lazy_string_substr = FUNTYPE(lib.lazy_string_substr)

# create the string
in_string = "abcdefghijklmnopqrstuvwxyz"
lib.lazy_string_create.argtypes = [ctypes.c_char_p]
lib.lazy_string_create.restype = ctypes.c_void_p
pointer = lib.lazy_string_create(in_string)

# create the ints
i_0 = 0
i_1 = 1
i_2 = 2
i_3 = 3
i_4 = 4
i_5 = 5
i_6 = 6
i_7 = 7
i_8 = 8
i_9 = 9
i_10 = 10
i_11 = 11
i_12
