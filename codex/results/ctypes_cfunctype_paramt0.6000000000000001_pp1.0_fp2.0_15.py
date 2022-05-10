import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_uint32)

##
# @brief A class representing the "object" of an instantiated class.
class PyObject(ctypes.Structure):
    pass

##
# @brief A class representing the "type" of an object.
class PyTypeObject(ctypes.Structure):
    pass

##
# @brief A class representing a Python module.
class PyModuleObject(ctypes.Structure):
    pass

##
# @brief A class representing a Python function.
class PyFunctionObject(ctypes.Structure):
    pass

##
# @brief A class representing a Python tuple.
class PyTupleObject(ctypes.Structure):
    pass

##
# @brief A class representing a Python list.
class PyListObject(ctypes.Structure):
    pass

##
# @brief A class representing a Python dict.
class PyDictObject(ctypes.Structure):
    pass

##
# @brief A class representing a Python string.
class PyStringObject(ctypes.Structure
