import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

def dot_product_submatrix_row_wise(matA, matB, col_limit):
    M = len(matA)
    N = len(matB[0]) if matB else 0
    K = len(matB) if matB else 0
    P = len(matA[0]) if matA else 0

    A_ = C.POINTER(C.c_int * P)
    B_ = C.POINTER(C.c_int * K)
    C_ = C.POINTER(C.c_long * P)
    matA_ = (A_ * M)(*map(A_, matA))
    matB_ = (B_ * K)(*map(B_, matB))
    shared = (C_ * M)(*(C_ * M)())
    local = (C_ * M)(*(C_ * M)())
    for i in xrange(M):
        for j in xrange(col_limit):
            local[i][j] = 0
    dimensions = numpy.array([
