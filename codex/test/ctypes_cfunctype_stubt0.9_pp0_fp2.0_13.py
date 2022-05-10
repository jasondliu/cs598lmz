import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hi there"

fun()  # "hi there"

fun.restype = ctypes.c_char_p
fun()  # b"hi there"


# customizations for using your own types instead of the default
# ones (PyCapsule objects): this is needed for accessing such objects from
# C++ code.

class PyFunHandler(object):
    def __init__(self, fun):
        self.fun = fun

    def __call__(self, *args):
        # the fun has to be called when PyFun_Handler is called,
        # hence the __call__ method
        r = self.fun(*args)
        print("PyFun_Handler called")
        return r


def c_pycapsule_from_pyfunc(fun):
    obj = PyFunHandler(fun)
    # return something that is not very correct, as it is readable we
    # don't need to care.
    return str(hash(obj))  # this is the "capsule".

# set the C api callbacks for registering/retrieving callbacks:

