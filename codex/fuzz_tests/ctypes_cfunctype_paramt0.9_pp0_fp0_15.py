import ctypes
FUNTYPE = ctypes.CFUNCTYPE(types.IntType,
                           ctypes.py_object, ctypes.py_object)
from ctypes.util import find_library
libc = ctypes.cdll.LoadLibrary(find_library("c"))
is_libc_new_enough = hasattr(libc, "is_digit")

def is_digit(space, w_obj):
    if not space.isinstance_w(w_obj, space.w_unicode):
        raise oefmt(space.w_TypeError, "expected unicode, got %T", w_obj)
    if not is_byte_compatible_unicode(w_obj):
        raise oefmt(space.w_ValueError,
                    "expected a narrow string, got %T",
                    w_obj)
    return space.newbool(
        is_libc_new_enough and libc.is_digit(w_obj.as_builtin_unicode())
        or ucd_is_digit(w_obj.as_unicode()[0])
    )
app_digit = space.appexec
