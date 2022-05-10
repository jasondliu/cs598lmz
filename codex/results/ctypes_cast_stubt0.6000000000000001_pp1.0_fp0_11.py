import ctypes
ctypes.cast(p, ctypes.py_object).value

#%%
def get_value_from_pointer(pointer):
    return ctypes.cast(pointer, ctypes.py_object).value

get_value_from_pointer(p)

#%%
class PyObject(ctypes.Structure):
    _fields_ = [('refcnt', ctypes.c_long)]

class PyIntObject(PyObject):
    _fields_ = [('ob_ival', ctypes.c_long)]

class PyStringObject(PyObject):
    _fields_ = [('ob_sval', ctypes.c_char * 1)]

class PyVarObject(PyObject):
    _fields_ = [('ob_size', ctypes.c_long)]

class PyListObject(PyVarObject):
    pass

class PyTupleObject(PyVarObject):
    pass

#%%
p = ctypes.py_object(1)
p

#%%
type(p)

#%%
ctypes.py_object.from_address(id(p
