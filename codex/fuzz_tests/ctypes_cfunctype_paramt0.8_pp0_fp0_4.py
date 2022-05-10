import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def callback(x, y):
    print "Got", x, y
    return 0

ptr = FUNTYPE(callback)

some_other_library.externally_defined_function(ptr)
</code>
However, notice that I have said nothing about Python in this code: it's just good old C-API Python, using the standard idiom for calling functions that expect a function pointer.
Your problems probably come from the fact that you are trying to mix C and C++. Mixing the two is usually not a good idea, and can complicate your life considerably. If you can rewrite the code and get rid of the C, do so. Otherwise, you need to learn how to use C++, and specifically how to write Python extension modules in C++.
Also, your code is really sloppy. You should really switch to using the Python <code>_types</code> module: <code>PyInt_FromLong</code> is deprecated, and is not available on Python 3, where you should be using <code>PyLong_FromLong</code> instead
