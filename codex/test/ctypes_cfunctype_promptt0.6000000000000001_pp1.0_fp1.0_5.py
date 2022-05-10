import ctypes
# Test ctypes.CFUNCTYPE
def test_cfuntotype():
    c_int_ptr = ctypes.POINTER(ctypes.c_int)
    c_int_ptr_ptr = ctypes.POINTER(c_int_ptr)
    c_int_ptr_ptr_ptr = ctypes.POINTER(c_int_ptr_ptr)
    c_int_ptr_ptr_ptr_ptr = ctypes.POINTER(c_int_ptr_ptr_ptr)

    # ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
    c_functype = ctypes.CFUNCTYPE(c_int_ptr_ptr_ptr_ptr, c_int_ptr, c_int_ptr_ptr, c_int_ptr_ptr_ptr)
    # 创建一个指向回调函数的指针
    callback = c_functype(test_cfuntotype)
    # 将回调
