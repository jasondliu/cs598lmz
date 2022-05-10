import ctypes
# Test ctypes.CFUNCTYPE(ctypes.c_bool)
print(ctypes.CFUNCTYPE(ctypes.c_bool)())
# Test ctypes.CFUNCTYPE(ctypes.c_bool)(),
print(ctypes.CFUNCTYPE(ctypes.c_bool)(),)
# Test ctypes.c_bool(ctypes.CFUNCTYPE(ctypes.c_bool)())
print(ctypes.c_bool(ctypes.CFUNCTYPE(ctypes.c_bool)()))
# Test ctypes.c_bool(ctypes.CFUNCTYPE(ctypes.c_bool)()),
print(ctypes.c_bool(ctypes.CFUNCTYPE(ctypes.c_bool)()),)
# Test ctypes.c_bool(ctypes.CFUNCTYPE(ctypes.c_bool)(),)
print(ctypes.c_bool(ctypes.CFUNCTYPE(ctypes.c_bool)(),))

# (1, 0) after import torch.nn
# Segmentation
