import ctypes
# Test ctypes.CFUNCTYPE
CFuncType = ctypes.CFUNCTYPE
# Test ctypes.CFunctionType
CFunctionType = ctypes.CFunctionType
# Test ctypes.PYFUNCTYPE
PyFuncType = ctypes.PYFUNCTYPE
# XXX: at_seq should not be exposed
ATSeq = ctypes.AT_seq
# Test ctypes.CFuncPtr
# XXX: test c_intptr_t and c_uintptr_t separately
cptr_0 = ctypes.CFuncPtr._ptr_type_(0)
cptr_0_name = ctypes.CFuncPtr.__name__
cptr_0_type = ctypes. CFuncPtr. _type_
cptr_0_class = ctypes. CFuncPtr. _class_
cptr_0_get_name = ctypes. CFuncPtr. _get_name_
# Test code paths in cython code not yet wrapped by tests
cptr_3 = ctypes.CFuncPtr.__new__(ctypes.CFuncPtr, 0, c_int_p, 'ptr
