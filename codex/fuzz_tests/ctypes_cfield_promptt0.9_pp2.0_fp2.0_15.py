import ctypes
# Test ctypes.CField subclass
# Load a given library, and return the corresponding ctypes.CDLL object.
# May raise OSError.
_libs = {}
_revision = 2
def dlopen(name, mode=ctypes.RTLD_LOCAL):
    if sys.platform == 'win32' and name.endswith('.dll'):
        name = name[:-4]
    flags = mode | ctypes.RTLD_GLOBAL
    for lib in _libs.values():
        if hasattr(lib, '_name') and name.endswith(lib._name):
            return lib
    return _libs.setdefault(name, ctypes.CDLL(name, mode=flags))

class Tcl_Obj(ctypes.Structure):
    pass

class Tcl_Interp(ctypes.Structure):
    pass

Tcl_Obj_String = ctypes.CFUNCTYPE(ctypes.c_char_p, ctypes.POINTER(Tcl_Obj))

Tcl_Interp_Result = ctypes.c_int
