import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# array of ints
intarr = ctypes.c_int * 5

# array of doubles
doublarr = ctypes.c_double * 10

# array of chars
chrarr = ctypes.c_char * 100

# array of int pointers
intptrarr = ctypes.POINTER(ctypes.c_int) * 10

# array of doubles pointers
dblptrarr = ctypes.POINTER(ctypes.c_double) * 10

# char pointers array
chrptrarr = ctypes.POINTER(ctypes.c_char) * 10

# char pointer to char array
chrptr = ctypes.POINTER(chrarr)

# array of function pointers
functptrarr = FUNTYPE * 10

# function pointer to function
functptr = FUNTYPE

# pointer to pointer to char
chrptrptr = ctypes.POINTER(chrptr)

# pointer to pointer to char array
chrptrptrarr =
