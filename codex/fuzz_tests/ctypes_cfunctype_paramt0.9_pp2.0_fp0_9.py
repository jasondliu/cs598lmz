import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_double, ctypes.c_int, ctypes.POINTER(ctypes.c_double))

#this function will be called from within the C library
# a is a double pointer to the address of an array
# i is the index of the array
    
def myfunc(x, ix, param):
    '''
    compute the weighted distance between points
    in c++ to get the address of array a, 
    you would use a[ix]
    '''
    result = 0.0
    wx, wy, wz = param[0], param[1], param[2]
    result = math.sqrt(X[ix]**2*wx + Y[ix]**2*wy + Z[ix]**2*wz)
    return result

# call the c library to update the results        
myCfunc = FUNTYPE(myfunc)
# c library
mylib = ctypes.cdll.LoadLibrary("/home/mike/dev/c/clib.so")

# initialize the
