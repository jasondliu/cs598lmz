import ctypes
# Test ctypes.CFUNCTYPE using a function that takes a file argument

# This function takes an open file and reads it.
def readsomefile(f):
    assert(f)
    x = f.read()
    assert(type(x) == str)
    return len(x)

# Declare some functions
my_func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(readsomefile)

filep = ctypes.c_void_p()
f = ctypes.pythonapi.PyFile_FromString('numbers.txt', 'r')
ctypes.pythonapi.PyFile_AsFile.restype = ctypes.py_object
filep = ctypes.pythonapi.PyFile_AsFile(f)

my_func(filep)
 
# Test ctypes.CFUNCTYPE using a function that returns a list
def func_return_list(i):
    return [i, i]

my_func2 = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.c_int
