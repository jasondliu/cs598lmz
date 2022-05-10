import ctypes
# Test ctypes.CFUNCTYPE
PYFUNC =  ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_int)
ctypes.cast( PYFUNC( pow ), ctypes.CFUNCTYPE( ctypes.c_double, ctypes.c_double, ctypes.c_double ) )

cbblas = ctypes.CDLL('cbblas_functions_so', RTLD_GLOBAL)
example=cbblas.example
example.restype = ctypes.c_int
example()

subroutine_test=cbblas.subroutine_test
subroutine_test.argtypes=(ctypes.c_double*4,)
subroutine_test( (100,100,100,100) )

pow(100,100)

sub1=cbblas.sub1
sub1.argtypes = (ctypes.c_float*2,)
sub1.restype = ctypes.c_float
sub1( (1.3,2.3) )
</code>

