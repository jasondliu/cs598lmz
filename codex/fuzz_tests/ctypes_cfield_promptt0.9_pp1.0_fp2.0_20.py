import ctypes
# Test ctypes.CField
# WARNING: The following check may or may not work depending the size of
#          classes in your libc.


class Struct2(ctypes.Structure):
    _fields_ = [("a", ctypes.c_long),
                ("b", ctypes.c_long),
                ("c", ctypes.c_char),
                (1, ctypes.c_int),
                ("d", ctypes.c_char),
                (2, ctypes.c_int),
                (3, ctypes.c_char),
                ("e", ctypes.c_long)]

try:
    ctypes.sizeof(Struct2)
except TypeError as details:
    if platform.system != 'SunOS':
        # SunOS seems to always support the more complicated features of
        # ctypes structures
        raise unittest.SkipTest("libc does not support overlapping "
                                "ctypes structure fields: " +
                                str(details))
    else:
        raise

# XXX: win64 has different alignment requirements :(
# (sizeof(long) == 4,
