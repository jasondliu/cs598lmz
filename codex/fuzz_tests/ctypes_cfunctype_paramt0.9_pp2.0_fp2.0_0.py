import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int))
def py_sum(xs):
    total = 0
    for x in xs:
        total += x
    return total

pysum = FUNTYPE(py_sum)
radius = 2
result = pow(4, 2) - pysum(ctypes.byref(result), radius)
print(result)
</code>
My question is:

any function pointer, and how many parameter should be passed in pysum, if you wanna use pysum as a callback function in C, also pass it as Py_BuildValue(O, pysum).
declare a pointer to ctypes.py_object is ok, such as c_pointer = ctypes.POINTER(ctypes.py_object)

Thanks advance.


A:

As already stated, you can't pass normal Python functions to C, at least not in this way. Either you need to rewrite your C function to call a Cython-cobject closure, like 
<code>void func(PyObject* callback)
{
    Py
