import ctypes
FUNTYPE = ctypes.CFUNCTYPE( ctypes.c_double, ctypes.c_int, ctypes.c_int )
ccsolver = FUNTYPE(solver.glpsolver.glpsolver_)
ccsolver.argtypes = [ ctypes.c_int,
                      ctypes.c_int,
                      ctypes.c_double,
                      ctypes.c_void_p,
                      ctypes.c_void_p,
                      ctypes.c_void_p ]
ccsolver.restype  = ctypes.c_double

def solve(A, b, g):
    """ 
    Solve the Lasso problem
     
        minimize 1/2 * \|A*x - b\|^2 + g * \|x\|_1
    
    using the homotopy continuation method described in the paper 

       "A homotopy method for l1-regularized problems"
       by 
       E. Candes, X. Li and M. Soltanolkotabi

    Parameters
    ----------

    A : (d,n) NumPy array
       Dictionary matrix
   
