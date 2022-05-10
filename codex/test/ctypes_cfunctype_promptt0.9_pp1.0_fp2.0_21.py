import ctypes
# Test ctypes.CFUNCTYPE will fail if too much parameters.
TEST_TYPE = ctypes.CFUNCTYPE(None, *[ctypes.c_uint8] * 512)

