import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class PyCFuncPtrObject(PyObject):
    _attrs_ = ["c_ob_type", "c_ob_refcnt", "c_ob_pypy_link",
               "c_cif_description", "c_callable", "c_args_types", "c_result_type",
               "c_wrap_callable"]
    _immutable_fields_ = ["c_args_types", "c_result_type", "c_wrap_callable"]
    _cif_description = "*x"

    def __init__(self, space, callable, args_types, result_type, wrap_callable):
        PyObject.__init__(self, space)
        self.c_callable = callable
        self.c_args_types = args_types
        self.c_result_type = result_type
        self.c_wrap_callable = wrap_callable

    def from_object(space, obj):
        if isinstance(obj, PyCFuncPtrObject):
            return obj
        raise OperationError
