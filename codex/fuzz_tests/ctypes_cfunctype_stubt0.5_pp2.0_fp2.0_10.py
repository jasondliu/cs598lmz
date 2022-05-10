import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print fun()
</code>
This code works fine, but I have a problem when I try to make the function return a string which is longer than a few characters.
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"*100

print fun()
</code>
This code prints the string "hello" 100 times and then segfaults.
I don't know why this happens, I have tried to return other types of objects and they work fine. Any ideas?


A:

You're returning a Python object from a C function.  The only way to do this is for the C function to create the object and return a pointer to it.  The C function does not know how to create a Python string object.  When you return a Python object from a C function, the interpreter is going to call Py_IncRef() on the object.  If you return a pointer to a local variable, the object will be destroyed when the function returns, and the interpreter will crash when it tries to increment the reference count
