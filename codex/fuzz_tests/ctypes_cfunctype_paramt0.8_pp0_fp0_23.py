import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.py_object)

#noinspection PyUnusedLocal
def _pyobj_to_double(o):
    try:
        return float(o)
    except TypeError:
        raise ValueError

#noinspection PyUnusedLocal
def _pyobj_to_long(o):
    try:
        i = int(o)
    except TypeError:
        raise ValueError
    #if the integer is larger than C long would allow, raise ValueError
    if i != int(ctypes.c_int(i).value):
        raise ValueError
    return i

_pyobj_to_c_char_p = ctypes.py_object

_c_char_p_to_pyobj = ctypes.c_char_p

_conversion_table = (
    ('double', _pyobj_to_double, ctypes.c_double),
    ('long', _pyobj_to_long, ctypes.c_int),
    ('char*', _pyobj_to_c_char_p
