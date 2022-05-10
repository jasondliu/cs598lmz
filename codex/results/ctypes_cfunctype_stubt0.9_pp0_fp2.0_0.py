import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print('hi')
    class BadClass(object): pass
    b = BadClass()
    return b

fun()
</code>
That gives the error:
<code>py_object(&lt;class '__main__.BadClass'&gt;) is bigger than 8 bytes!
</code>
Which makes sense in that the object pointer is 4 bytes on 32-bit and 8 bytes on 64-bit, but the context pointer is also 4 bytes on 32-bit and 8 bytes on 64-bit, so you cannot return a PyObject* + the context of the function in a C type.
It is possible to hack around this with memoryviews, but it is nasty. If a Python class object is returned, you will have to write specialized Python functions in C to deal with them, or implement enough of a CPython runtime in C to handle classes, functions and so on. This could be a long and hard road, depending on what you want to do! A pure C extension might work better.

