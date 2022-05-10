import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return my_callback(1)
assert fun() == 42
</code>
This works.
Hopefully that's what you need.
EDIT: I just realized that I should probably explain why this works. The reason is that, as explained in the question, in C++ the callback is a member variable, so when the callback is invoked from the native code, there's always an instance of the class to get the function from. In Python, there's no such guarantee. So to work around it, we pass a "global variable" in the form of a function pointer with a closure. The closure simply captures the reference to the <code>my_callback</code> function, which is assumed to be globally accessible from the native code.

