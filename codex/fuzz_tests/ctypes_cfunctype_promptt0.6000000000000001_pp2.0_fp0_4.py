import ctypes
# Test ctypes.CFUNCTYPE()
import _ctypes_test
with _ctypes_test.Dll() as dll:
    if dll.test_cfuncptr_0() != 0:
        print("test_cfuncptr_0() failed")
    if dll.test_cfuncptr_1() != 1:
        print("test_cfuncptr_1() failed")
    if dll.test_cfuncptr_2() != 2:
        print("test_cfuncptr_2() failed")
    if dll.test_cfuncptr_3() != 3:
        print("test_cfuncptr_3() failed")
    if dll.test_cfuncptr_4() != 4:
        print("test_cfuncptr_4() failed")
    if dll.test_cfuncptr_5() != 5:
        print("test_cfuncptr_5() failed")
    if dll.test_cfuncptr_6() != 6:
        print("test_cfuncptr_6() failed")
    if dll.test_cfuncptr_7() !=
