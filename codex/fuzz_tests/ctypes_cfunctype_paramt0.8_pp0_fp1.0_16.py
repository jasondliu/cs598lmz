import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
# function that takes a function pointer as an arg and returns it's value
def func(callable):
    return callable(5)

def main():
    # declare a function pointer that takes an int and returns an int
    ftp = FUNTYPE()
    # try to assign the python function to the function pointer and pass it
    # to the other python function.
    ftp.value = func(ftp)

if __name__ == '__main__':
    main()
</code>

