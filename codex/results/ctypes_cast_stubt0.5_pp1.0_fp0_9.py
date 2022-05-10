import ctypes
ctypes.cast(0, ctypes.py_object).value

# this is a little more powerful, but also more dangerous
# it allows you to cast any address as a python object
# if the address happens to be the address of a python object
# that is accessible, you can "reach in" and look at its contents
# note that it is not safe to dereference the pointer, only to look
# at its contents, since it may not be a real python object
ctypes.pythonapi.PyCapsule_GetPointer.restype = ctypes.c_void_p
ctypes.pythonapi.PyCapsule_GetPointer.argtypes = [ctypes.py_object, ctypes.c_char_p]
def pymem(address, module_name=None):
    name = "<%s>" % id(module_name) if module_name else None
    return ctypes.pythonapi.PyCapsule_GetPointer(ctypes.py_object(address), name)

# use objgraph to find all references to a given object
import objgraph
def get_all_references(obj
