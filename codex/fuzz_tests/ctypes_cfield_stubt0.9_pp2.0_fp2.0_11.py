import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def gnu_asprintf(buf, fmt, foo_ptr):
    ctypes.pythonapi.PyOS_snprintf(ctypes.byref(buf), ctypes.c_ulong(0xFFFF), ctypes.byref(fmt), foo_ptr)

get_name = ctypes.pythonapi.PyStructSequence_GetName
get_name.argtypes = [ctypes.py_object]
get_name.restype = ctypes.c_char_p

for struct_name in ('stat', 'statvfs', 'flock'):
    for suffix in ('', '_result'):
        for kind in ('', '_T'):
            typename = "{}_struct{}{}".format(struct_name, suffix, kind)
            if not hasattr(ctypes, typename):
                continue

            type = getattr(ctypes, typename)
            buf = ctypes.create_string_buffer(2048) # Fixme: Find exact size
            for field in type._fields_[:-1]: # Skip st_pad
                fmt
