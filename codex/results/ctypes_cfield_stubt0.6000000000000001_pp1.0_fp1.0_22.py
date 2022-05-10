import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class My_CFunction(ctypes.CFunctionType):
    _fields_ = [('_restype_', ctypes.c_int),
                ('_argtypes_', ctypes.POINTER(ctypes.c_int)),
                ('_flags_', ctypes.c_int)]

def callfunc(func, args):
    return func(*args)

def main():
    # This is a C function that returns an integer, and takes a pointer to an
    # integer as an argument.
    func = My_CFunction(callfunc)

    # Make a Python list of integers.
    lst = [1, 2, 3]

    # Get a pointer to the first element of the list.
    ptr = lst[0]

    # Call the C function.
    print(func(ptr))

main()
</code>

