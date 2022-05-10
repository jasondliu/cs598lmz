import ctypes
# Test ctypes.CFUNCTYPE
------------------------
if __name__ == "__main__":
    # Define C functions
    #-------------------
    # typedef void (*afunc)(void);
    # double square(double);
    # long factorial(int);
    # double sine(double,int);

    if platform.system() == 'Linux':
        mydll = ctypes.CDLL('libc.so.6')
    elif platform.system() == 'Windows':
        mydll = ctypes.CDLL('msvcrt.dll')

    # Create CFUNCTYPEs for C functions
    #----------------------------------
    # void (*afunc)(void);
    farg = [] #void (*afunc)(void);
    functype1 = ctypes.CFUNCTYPE(None, *farg)

    # double square(double);
    farg = [ctypes.c_double]
    functype2 = ctypes.CFUNCTYPE(ctypes.c_double, *farg)

    # long factorial(int);
    farg = [ctypes.c
