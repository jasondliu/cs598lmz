import ctypes
ctypes.cast(0, ctypes.py_object)

# Next we test whether the C type provided by the Python 2 extension
# module pickle gives the correct results.  The type's constructor
# takes an integer argument, the address of the object to cast to.
# Testing it is optional:
try:
    from _testcapi import INT_FROM_PTR
except ImportError:
    no_c_cast_to_py_object = True
    def cast_to_py_object(x):
        raise SkipTest("_testcapi.INT_FROM_PTR unavailable")
else:
    no_c_cast_to_py_object = False
    from capi_tests import cast_to_py_object, INT_FROM_PTR

# The C type provided by the Python 3 extension module pickle gives a
# TypeError for non-integral objects, but a ValueError for integral
# objects that aren't pointers.
def cast_to_py_object_py3(x):
    try:
        c = cast_to_py_object(x)
    except TypeError
