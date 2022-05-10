import ctypes
# Test ctypes.CFUNCTYPE()
qcomdl_common.pfn_qcomdl_get_version = ctypes.CFUNCTYPE(
    ctypes.c_int,
    ctypes.c_int,
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_int))

# Test ctypes.windll.LoadLibrary()
qcomdl_dll = ctypes.windll.LoadLibrary("M:\\0001956783_L45\\mdt_test_suite\\qtap_msm\\MDT_339\\files\\lib\\qdl_wrapper.dll")
print("Access to MPROC module using ctypes.windll.LoadLibrary()\n")

# Test ctypes.WinDLL()
qcomdl_dll = ctypes.WinDLL("M:\\0001956783_L45\\mdt_test_suite\\qtap_msm\\MDT_339\\files\\
