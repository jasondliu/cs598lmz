import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

###########
# complex #
###########
cmplx = ctypes.c_double(2.0 + 3.0j)
print(cmplx.real)
print(cmplx.imag)
##########################
# Complex numbers in C99 #
##########################
# https://gcc.gnu.org/onlinedocs/gcc/_005fComplex.html
# gcc -fcomplex-010 _Complex.c -o _complex
# Reference:
# https://www.gnu.org/savannah-checkouts/gnu/libiberty/cplus-dem.c
# HP-UX gcc -o complex complex.c
#import sys
#sys.path.append("/home/yhuang9/Desktop/c/")
import _Complex
print(ctypes.sizeof(_Complex.float))
print(ctypes.sizeof(_Complex.double))
print(ctypes.sizeof(_Complex.longdouble))
def complex_add(a, b):
    return _Complex.float(a.real + b.
