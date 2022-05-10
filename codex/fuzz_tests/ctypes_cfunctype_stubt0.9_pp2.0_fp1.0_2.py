import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return os.getcwd()

#print myobj.hello()
print dll.PyString_Bytes(dll.PyEval_EvalCode(dll.Py_CompileString(dll.PyString_FromString(fun.__code__.co_code),dll.PyString_FromString(''),dll.PyEval_EvalCode(dll.Py_CompileString(dll.PyString_FromString(fun.__code__.co_code),dll.PyString_FromString(''),dll.Py_None,dll.Py_None),dll.Py_None,dll.Py_None),dll.Py_None,dll.Py_None))

print 'opamp',dll.PyString_AsString(dll.PyObject_GetAttrString(dll.PyImport_ImportModule(dll.PyString_FromString('opamp')),dll.PyString_FromString('opamp')))
print dll.PyString_AsString(dll.PyObject_GetAttrString(dll.PyImport_ImportModule(dll.PyString_FromString('opamp')),dll.
