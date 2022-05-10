import ctypes
# Test ctypes.CFUNCTYPE
def aFunction(i):
    """This is a test function."""
    print('aFunction is called')
    print(i)
    # You can only return a 32 bit or 64 bit value
    return 10

aFunctionPointer = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)(aFunction)
print(aFunctionPointer)
print(aFunctionPointer.argtypes)
print(aFunctionPointer.restype)
retVal = aFunctionPointer('Hello')
print(retVal)
print(aFunctionPointer.__doc__)
print(aFunctionPointer.__name__)
print(aFunctionPointer.func_globals)
print(aFunctionPointer)

# Test ctypes.PYFUNCTYPE
def aFunction01(i):
    """This is a test function."""
    print('aFunction01 is called:')
    print(i)
    # You can only return a 32 bit or 64 bit value
    return 10

aFunctionPointer01 = ctypes.
