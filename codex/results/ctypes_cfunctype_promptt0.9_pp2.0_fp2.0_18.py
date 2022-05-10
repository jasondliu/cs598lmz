import ctypes
# Test ctypes.CFUNCTYPE

mp_int = ctypes.c_int

def py_int_to_int(n):
    assert isinstance(n, int)
    return ctypes.c_int(n)

mp_int_convert = ctypes.CFUNCTYPE(mp_int, py_int_to_int)

def CFUNCTYPE_test():
    mp_int_convert(42)
    try:
        mp_int_convert('42')
    except TypeError:
        pass
    else:
        print 'expected TypeError, did not get it'

#------------------------------

# Test ctypes.WINFUNCTYPE

def WINFUNCTYPE_test():
    HANDLE = ctypes.c_int
    DWORD = ctypes.c_ulong
    LPCTSTR = ctypes.c_char_p

    CreateThread = ctypes.WINFUNCTYPE(HANDLE,              # _Return_type_
                                      DWORD,              # _Formal_parameters_
                                      DWORD,
                                     
