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
