import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

crash = fun()
crash()

# The crash is:
# Fatal Python error: GC object already tracked
# Segmentation fault (core dumped)
</code>

I don't understand the error message. I thought that the <code>CFUNCTYPE</code> was supposed to convert a Python function to a C function. 
I don't understand why the crash occurs.

I understand that <code>CFUNCTYPE</code> is used to convert between Python and C functions, but I don't understand what's going on when <code>CFUNCTYPE</code> is used on a Python function. I'm guessing that it's creating a C function that's returning the Python <code>None</code> object, and then the C function is being called from the Python code, but I'm not sure what's happening.
Then I'm guessing that the <code>fun()</code> is returning the Python <code>None</code> object, but that somehow ends up being a "GC object already tracked", whatever that means.
I'm guessing that I'm getting the crash because there's a garbage collection issue
