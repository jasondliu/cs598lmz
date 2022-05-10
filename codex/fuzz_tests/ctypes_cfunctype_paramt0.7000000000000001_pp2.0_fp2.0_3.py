import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int)

class PyCFuncObject(ctypes.Structure):
    _fields_ = [('ob_refcnt', ctypes.c_long),
                ('ob_type', ctypes.c_long),
                ('func_doc', ctypes.c_long),
                ('func_name', ctypes.c_long),
                ('func_globals', ctypes.c_long),
                ('func_defaults', ctypes.c_long),
                ('func_code', ctypes.c_long),
                ('func_closure', ctypes.c_long),
                ('func_closure', ctypes.c_long),
                ('func_weakreflist', ctypes.c_long),
                ('func_dict', ctypes.c_long),
                ('func_module', ctypes.c_long),
                ('func_methargs', ctypes.c_long),
                ('func_methvarargs', ctypes.c_long),
                ('func_methkeywords', ctypes.
