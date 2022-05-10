import ctypes
ctypes.cast(a, ctypes.POINTER(ctypes.c_int))

# @numba.jit(nopython=True)
# def test_numba(a):
#     a[0] = 1
#     return a
#
# a = np.zeros((2, 2), dtype=np.int32)
# test_numba(a)
# print(a)
