import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("captured")
</code>
But as soon as I want to use <code>x</code> in the function, it won't do:
<code>FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
@FUNTYPE
def fun(x):
    print("captured", x)
</code>
It works, but the same behaviour.
I don't know how to work with it? If I am interested in <code>n</code> function-specific values, I could put them in a machine-word? But I want tool to be independent of the used word-size (just like higher-order functions).
I'm also confused about the used <code>py_object</code> type. As far as I understand from here, it is a "<code>PyObject*</code>", that is - a void-pointer. But I can see that it is a struct-type in ctypes (which is specified in <code>Python.h</code>'s <code>typedef struct _object PyObject</code>).
There are posts like this
