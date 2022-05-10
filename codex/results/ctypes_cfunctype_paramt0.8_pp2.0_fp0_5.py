import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)
def MyPyCallback():
    print('Callback!')

func = FUNTYPE(MyPyCallback)

# Call a C library, who calls back our callback when it is ready
ctest.register_callback(func)
ctest.do_something_in_c()
</code>
This works, but I find it very low level. You have to specify the type of the callback and then convert it to a C function pointer (using <code>FUNTYPE</code>) in order to pass it to the C library.
Is there a way to pass a python function as a parameter to a C function, without using ctypes? Any other suggestions on how to achieve this in a more pythonic way?


A:

You can use the Cython library to do this.
Here's a minimal example. While you could use it as a compiled extension, it's also completely reasonable to use it as a code generator, with the generated extension code then being imported directly.
<code>cython_example.pyx</code>:
<code>cdef extern from "ctest.h":
    void do_something_in_c(
