import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_int)

# This function takes a function pointer as argument, and call it
def call_func(fptr, n):
    return fptr(n)

def main():
    # A python function, to be passed as argument
    def pyfunc(n):
        return n * 10
    # Get the function pointer
    fptr = FUNTYPE(pyfunc)
    # Call the function through the pointer
    result = call_func(fptr, 100)
    print(result)

main()
</code>

