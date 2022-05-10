import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def test_get_function_addr():
    # Check that we can get the address of a function.
    #
    # This is a problem on Windows, if we compile the function
    # with a toolchain other than MSVC.  The reason is that
    # the C compiler and the MSVC linker don't agree on the
    # mangling of the name of the function.  The _ctypes
    # extension uses MSVC, so the linker cannot find the
    # function.  It happens that this test only fails if the
    # function is not inlined.
    addr = lltype.cast_ptr_to_int(llhelper(lltype.Ptr(FUNTYPE),
                                           fun.getaddr()))
    assert addr != 0

def test_addressof():
    # Check that we can get the address of a function.
    #
    # This is a problem on Windows, if we compile the function
    # with a toolchain other than MSVC.  The reason is that
    # the C compiler and the MSVC linker don't agree on the

