import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double()
    y = ctypes.c_double()
    z = ctypes.c_double()

class StructWrapper:
    def __init__(self, ctype, python_object):
        # store the ctypes object
        self.ctype = ctype

        # store the python object
        self.python_object = python_object

    def __getitem__(self, key):
        # get the value from the ctypes object
        # and return it
        return getattr(self.ctype, key)

class PyType(ctypes.c_double):
    # define the new object
    # it's a c_double and has a python object stored in it
    def __new__(cls, value, python_object):
        # initialize the c_double
        obj = ctypes.c_double.__new__(cls, value)

        # initialize the StructWrapper
        obj.python_object = StructWrapper(obj, python_object)

        # return the c_double
        return obj

    # redefine the access
