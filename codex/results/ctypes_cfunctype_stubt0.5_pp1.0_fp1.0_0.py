import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return (1,2,3,4,5)

print fun()
</code>
I'm using Python 2.6.6.  I've tried this on both Windows and Linux.  Am I doing something wrong?  Is there a way to do this?
Thanks!


A:

The problem is that <code>ctypes</code> does not know how to convert a <code>tuple</code> to a C pointer.  You need to tell it how to do that.  The easiest way is to make a <code>ctypes</code> array type.  So, for example:
<code>import ctypes

# Get the C types that we need
int_type = ctypes.c_int
int_ptr_type = ctypes.POINTER(int_type)

# Make a ctypes array type to hold the tuple
array_type = int_type * 5

# Define the function
@ctypes.CFUNCTYPE(int_ptr_type)
def fun():
    return array_type(1, 2, 3, 4, 5)

# Test it
