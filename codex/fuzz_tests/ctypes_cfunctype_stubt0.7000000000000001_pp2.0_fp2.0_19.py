import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    c = a
    return c

print fun()

# This is another way to call the function
print FUNTYPE(fun)()
</code>
Output
<code>Hello World
Hello World
</code>
I do understand that this is a simple example. I just want to know how to pass a python variable to the ctypes function and how to use the ctypes function in the python code.


A:

In your example the C function doesn't actually return the value of the global variable. Instead it returns the value of the local variable <code>c</code>. The local variable <code>c</code> is initialized with the value of the global variable <code>a</code>. In other words, the local variable <code>c</code> is a copy of the global variable <code>a</code>.
You might think that the C function doesn't copy the value of the global variable and that the local variable is a reference to the global variable. However, that is not the case. In C, all variables have local scope by default. This means that variables defined inside the function will only be visible inside the function. If you want a variable to
