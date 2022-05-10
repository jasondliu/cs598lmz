import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def myfunc(x):
    return x**2

fptr = FUNTYPE(myfunc)
print fptr(5.0)
</code>
Here, I have defined a function <code>myfunc</code> and then I have created a pointer to that function using <code>FUNTYPE</code>. 
Now, let's say I have a <code>C</code> function that takes a pointer to a function as an argument. How can I call that function from <code>Python</code>?
EDIT:
I have come up with this code:
<code>import ctypes

def myfunc(x):
    return x**2

fptr = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)(myfunc)

lib = ctypes.CDLL("libmylib.so")
lib.my_c_function.argtypes = [ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)]
lib.my_c_function
