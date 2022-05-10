import ctypes
# Test ctypes.CField
def aFunction(obj):
  print(obj)
CF = ctypes.CField(aFunction)
assert ctypes.sizeof(CF) == ctypes.sizeof(ctypes.c_void_p)
class StructWithFunction(ctypes.Structure):
    _fields_ = [("name", ctypes.c_char),
                ("address", ctypes.c_char),
                ("ptr_to_function", CF)]
# It is legal to let compiler (MSVC or CLANG) decide the alignment of the object
with suppress_warnings():
    from fast_c.forwarded_fields import UniqueInlinedFunctionSized, UniqueInlinedFunctionSizedPtr
    UniqueInlinedFunctionSized.__ctype_be__ = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(StructWithFunction))
    UniqueInlinedFunctionSizedPtr.__ctype_be__ = ctypes.POINTER(UniqueInlinedFunctionSized)
    add_c_line("\nunique_inlined_functionsized = UniqueInlinedFunctionSized(lambda
