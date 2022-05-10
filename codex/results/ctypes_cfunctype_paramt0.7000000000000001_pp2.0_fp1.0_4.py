import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.py_object)

#Module data
MODULE_FILE = os.path.join(os.path.dirname(__file__), '_fmodpy.so')
_fmodpy = ctypes.CDLL(MODULE_FILE)
_fmodpy.fmodpy_create.argtypes = [ctypes.POINTER(ctypes.py_object)]
_fmodpy.fmodpy_create.restype = ctypes.c_void_p
_fmodpy.fmodpy_set_params.argtypes = [ctypes.c_void_p, ctypes.py_object]
_fmodpy.fmodpy_set_params.restype = None
_fmodpy.fmodpy_run.argtypes = [ctypes.c_void_p, FUNTYPE]
_fmodpy.fmodpy_run.restype = None
_fmodpy.fmodpy_delete.argtypes = [ctypes.c_void_p]
_fmodpy.fmodpy_delete.restype = None

#Py
