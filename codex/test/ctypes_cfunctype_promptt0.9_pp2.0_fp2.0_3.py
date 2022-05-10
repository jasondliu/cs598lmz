import ctypes
# Test ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_double, 
#                        ctypes.POINTER(ctypes.c_double))
#c_double_p=ctypes.POINTER(ctypes.c_double)
#print c_double_p
#my_type=ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_double, c_double_p)
#Id=my_type(lambda a,b,c : print(a,b,c[0]))
#Id(42,4.2,ctypes.c_double(4.4))


# Regular tests

# Test C++ wrapping of python functions

def test_fun(i) :
    print("Calling Python function with i = %d" % i)
    return i**2

print("Creating function in Python")
