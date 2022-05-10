import ctypes
ctypes.cast(dst, ctypes.c_void_p).value)

Dst = image.dtype

map_func = cuda.jit('void(uint8[:], uint8[:], uint8[:], int32[:], int32[:], int32[:], int32[:], int32[:], int32[:], int32[:])')
def affine_map_single(dst, image, mask, trans, shift, a_src, b_src, c_src, a_dst, b_dst, c_dst):
    i, j = cuda.grid(2)
    n, m = image.shape
    if i < n and j < m:
        x = (j - shift[0])*trans[0] - (i - shift[1])*trans[1]
        y = (j - shift[0])*trans[2] - (i - shift[1])*trans[3]
        if image[i,j] != 0:
            dst[i,j] = 0
        else:
            try:
