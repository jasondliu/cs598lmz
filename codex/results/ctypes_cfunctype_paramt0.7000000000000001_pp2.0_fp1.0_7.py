import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double)
FORTE_PI = FUNTYPE(('for_PI', FORTE_LIB))

##
# \brief Return the square root of a double
def sqrt(x):
    return ctypes.c_double.in_dll(FORTE_LIB, 'for_SQRT').value * x

##
# \brief Return the exponential of a double
def exp(x):
    return ctypes.c_double.in_dll(FORTE_LIB, 'for_EXP').value * x

##
# \brief Return the exponential base 10 of a double
def exp10(x):
    return ctypes.c_double.in_dll(FORTE_LIB, 'for_EXP10').value * x
    
##
# \brief Return the exponential base 2 of a double
def exp2(x):
    return ctypes.c_double.in_dll(FORTE_LIB, 'for_EXP2').value * x
    
##
# \brief Return the natural logarithm of a double
def ln(x):
   
