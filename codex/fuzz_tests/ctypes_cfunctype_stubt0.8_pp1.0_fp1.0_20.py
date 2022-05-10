import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print "fun()"
os.environ['PYTHON_EMBEDDED_INTROSPECT'] = '1'
os.environ['PYTHON_EMBEDDED_CALLBACKS'] = '1'
ctypes.pythonapi.PyImport_ImportModule.argtypes = [ctypes.c_char_p]
ctypes.pythonapi.PyImport_ImportModule.restype = ctypes.py_object
import_global = ctypes.pythonapi.PyImport_ImportModule
embedded_module = import_global('embedded')
pysig_connect_global = embedded_module.pysig_connect
pysig_connect_global.argtypes = [ctypes.py_object, ctypes.py_object]
pysig_connect_global(ctypes.py_object(fun), ctypes.py_object('mysignal'))
del pysig_connect_global

#class funobj(ctypes.Structure):
#    _fields_ = [('cb', ctypes.CFUNCTYPE(ctypes.
