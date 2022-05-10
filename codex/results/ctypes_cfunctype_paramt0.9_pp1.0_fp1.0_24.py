import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_uint,ctypes.POINTER(ctypes.c_uint),ctypes.POINTER(ctypes.c_uint))

lib = ctypes.CDLL("SharedLibraryWrapper.dll")

def foo(a,b,c):
    alpha, omega, theta = 1, 2, 3
    lib.fortunes.restype = FUNTYPE
    f = lib.fortunes(alpha,omega,theta)
    return f(a,b,c)

if "__main__" == __name__:
    a,b,c = 6,4,244
    f = foo(a,b,c)
    print(f)
</code>
The question that I have is: What is the right way to pass generic callable python object as argument to c++ function?
I know this works. I want to know some better way than specifying the type of python callable each and every time I use it.
Please Help if you can.
Thanks!
EDIT: I just realized I can pass a function object as argument (create a wrapper class in c++) -
