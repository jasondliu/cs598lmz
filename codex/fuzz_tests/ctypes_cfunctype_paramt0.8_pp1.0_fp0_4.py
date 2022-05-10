import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double)

def func_double(f):
    return FUNTYPE(f)


def func_int(f):
    return ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(f)


def func_void(f):
    return ctypes.CFUNCTYPE(None)(f)


def get_func_argtypes(f):
    return ctypes.restype(f)


class _StructMeta(type):

    def __new__(cls, class_name, bases, attrs):
        """
        Create struct class with the fields in attrs as attributes
        """
        if "fields" in attrs:
            fields = attrs["fields"]
            del attrs["fields"]
        else:
            fields = {}
        attrs["fields"] = fields
        return super(_StructMeta, cls).__new__(cls, class_name, bases, attrs)

    def __init__(cls, class_name, bases, attrs):
        super(_StructMeta, cl
