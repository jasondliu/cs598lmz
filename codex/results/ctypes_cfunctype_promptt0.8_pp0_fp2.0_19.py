import ctypes
# Test ctypes.CFUNCTYPE
def test_cfuntotype():
    test_struct = ctypes.c_int(0)
    test_pointer = ctypes.pointer(test_struct)
    
    def Test_Function(ptr):
        global test_struct
        test_struct.value = 5
        
    test_cfunc = ctypes.CFUNCTYPE(None, ctypes.POINTER(ctypes.c_int))(Test_Function)
    test_cfunc(test_pointer)
    assert test_struct.value == 5
test_cfuntotype()
# Test ctypes.byref
def test_byref():
    test_cint = ctypes.c_int(1)
    test_pointer = ctypes.byref(test_cint)
    assert test_pointer[0] == 1
test_byref()
# Test ctypes.string_at
def test_string_at():
    test_cint = ctypes.c_int(1)
    test_pointer = ctypes.pointer(test_cint)
    test_string = ctypes.string_
