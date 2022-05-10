import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def quadprog(P, q, G, h, A, b):
    # P is n x n, q is n x 1, G is m x n, h is m x 1, A is p x n, b is p x 1.
    n = P.shape[0]
    m = G.shape[0]
    p = A.shape[0]

    # We need to transpose G and h because the quadprog function expects
    # the arguments in the other order.
    P = P.T.copy()
    q = q.copy()
    G = G.T.copy()
    h = h.copy()
    A = A.T.copy()
    b = b.copy()

    # Create the quadprog function.
    quadprog = FUNTYPE(('quadprog', quadprog_lib), ((1, 'n'), (1, 'm'), (1, 'p'), (n, 'P'), (n, 'q'), (m, 'G'), (m, 'h
