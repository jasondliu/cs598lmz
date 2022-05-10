import ctypes
# Test ctypes.CField
import ctypes.test.test_cfield
ctypes.test.test_cfield.main()

# Test ctypes.CFuncPtr
import ctypes.test.test_cfunctype
ctypes.test.test_cfunctype.main()

# Test ctypes.CStruct
import ctypes.test.test_cstruct
ctypes.test.test_cstruct.main()

# Test ctypes.CUnion
import ctypes.test.test_cunion
ctypes.test.test_cunion.main()

# Test ctypes.CArray
import ctypes.test.test_carray
ctypes.test.test_carray.main()

# Test ctypes.POINTER
import ctypes.test.test_pointer
ctypes.test.test_pointer.main()

if sys.platform != "win32":
    # Test ctypes.Structure
    import ctypes.test.test_structures
    ctypes.test.test_structures.main()

    # Test ctypes.Union
    import ctypes.test.test_
