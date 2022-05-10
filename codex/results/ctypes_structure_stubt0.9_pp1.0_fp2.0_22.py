import ctypes

class S(ctypes.Structure):
    x = ctypes.Structure
    _fields_ = [("s", ctypes.c_char_p)]


def invoke_from_python_from_c(*args):
    from pypy.module.cpyext.test.test_capi import capi
    argv = rffi.cast(capi.PY_SSIZE_T_P, args[0])
    argc = rffi.cast(lltype.Signed, args[1])
    for i in xrange(argc):
        addr = rffi.ptradd(rffi.cast(rffi.CCHARP, argv), i*sizeofaddr)
        String = rffi.cast(capi.PY_STRING_PTR, addr)[0]
        print rffi.charp2str(capi.PyString_AS_STRING(String))


PY_FROM_C_FUNC = lltype.Ptr(lltype.FuncType([llmemory.Address, lltype.Signed],
                                            lltype.Void))

T
