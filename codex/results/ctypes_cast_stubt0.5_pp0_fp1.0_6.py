import ctypes
ctypes.cast(0, ctypes.c_void_p)

# /usr/include/x86_64-linux-gnu/bits/stdio2.h:100:5
try:
    __off64_t = ctypes.c_long
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/stdio2.h:100:5
try:
    __off64_t = ctypes.c_longlong
except:
    pass

off64_t = __off64_t  # /usr/include/x86_64-linux-gnu/bits/types.h:146

# /usr/include/x86_64-linux-gnu/bits/types.h:147:9
class struct_stat(ctypes.Structure):
    pass

stat = struct_stat  # /usr/include/x86_64-linux-gnu/sys/stat.h:104

stat64 = struct_stat  # /usr/include/x86_64-linux-gnu/sys/stat.h:113

# /
