import ctypes

class S(ctypes.Structure):
    x = ctypes.Union[long, Exception]

lib.llvm.test.test_inl_union.s = S
