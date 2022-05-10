import ctypes
# Test ctypes.CFUNCTYPE
!gcc -xc -S -o /dev/stdout -O3 ./cpp_src/ctypesCFUNCTYPE.cpp 2> /dev/null

fp = lambda: None
ctypes.CFUNCTYPE(ctypes.c_int)(fp)
type(ctypes.CFUNCTYPE(ctypes.c_int)(lambda: None)._type_)
!gcc -xc -S -o /dev/stdout -O3 ./cpp_src/ctypesARRAY.cpp 2> /dev/null
NUM_ELEMS = 5

l = ctypes.c_int * NUM_ELEMS
a = l() # this line is relatively expensive
a = l([0] * NUM_ELEMS)
a[3]
!gcc -xc -S -o /dev/stdout -O3 ./cpp_src/ctypesPOINTER.cpp 2> /dev/null
intp = ctypes.POINTER(ctypes.c_int)
!gcc -xc -S -o /dev/stdout -O3 ./cpp_src/
