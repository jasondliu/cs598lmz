import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double)

# Define a ctypes function wrapper around the adaptor
cwrapper = FUNTYPE(C_adaptor_wrapper)
</code>
However, I'm a bit lost when it comes to passing the Python arguments from the ctypes function wrapper to the Python adaptor. 
<code>def C_adaptor_wrapper(pyfunc, x):
    # Define adaptor function called on a C wrapper
    def adaptor(x):
        return pyfunc(x).real
    return adaptor(x)
</code>
I read that the first argument to the wrapper function is always the instance of the calling instance, but this doesn't seem to be the case for my example. I also read that I can pass the Python function as a parameter, but I don't know how to define the ctypes function wrapper to accept a "pointer to a pointer".
Has anyone done this before? Any help would be appreciated.


A:

You can pass any variable to C (and use it inside the C code) if you convert it to ctypes object.
You need to store the given function object in a global variable (c
