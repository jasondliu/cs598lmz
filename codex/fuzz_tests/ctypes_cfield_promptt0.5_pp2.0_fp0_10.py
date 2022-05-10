import ctypes
# Test ctypes.CField.from_address()
import _ctypes_test

if __name__ == "__main__":
    lib = ctypes.CDLL(_ctypes_test.__file__)
    fld = ctypes.CField.from_address(lib._testfunc_p_p, ctypes.POINTER(ctypes.c_void_p))
    print(fld.type)
    print(fld.offset)
    print(fld.size)
    print(fld.bitshift)
    print(fld.bitsize)
    print(fld.type._length_)
    print(fld.type._type_)
    print(fld.type._flags_)
    print(fld.type._alignment_)
    print(fld.type._ffiargshape)
    print(fld.type._ffishape)
    print(fld.type._flags_ & ctypes.FUNCFLAG_CDECL)
    print(fld.type._flags_ & ctypes.FUNCFLAG_USE_ERRNO)
    print
