import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    pass
fun.ctypes = common.ctypes.FunctionType(common.ctypes.DefaultCallConvention,
                                        common.ctypes.UnknownType,
                                        (fun,),
                                        {})

# test CommonType.from_address
PyType_Type = common.types['PyType_Type']
ctypes.cast(ctypes.py_object(PyType_Type), common.ctypes.POINTER(common.ctypes.UnknownType))[0]

# test PYFUNCTYPE
PyObject_Call = common.functions['PyObject_Call']
call_func = PyObject_Call()
call_func.ctypes = common.ctypes.FunctionType(common.ctypes.DefaultCallConvention,
                                              common.ctypes.UnknownType,
                                              (call_func,),
                                              {})
assert call_func(None, 0) is common.NotImplemented
assert call_func(None, None) is common.NULL
assert call_func(PyType_Type, ()) == PyType_Type

# test PyArg
