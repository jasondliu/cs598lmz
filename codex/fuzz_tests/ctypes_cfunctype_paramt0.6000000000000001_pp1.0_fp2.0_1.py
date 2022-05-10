import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p)

def function_pointer(f):
    f.__void_ptr__ = FUNTYPE(f)
    return f

_lib = None
def _get_library():
    global _lib
    if _lib is None:
        _lib = ctypes.CDLL(find_library('SDL2'))
    return _lib

def _SDL_version(version):
    if isinstance(version, Version):
        return version
    else:
        return Version(version)

class _SDL_version_p(ctypes.Structure):
    _fields_ = [('major', ctypes.c_ubyte),
                ('minor', ctypes.c_ubyte),
                ('patch', ctypes.c_ubyte)]
    def __init__(self, version):
        self.major = version.major
        self.minor = version.minor
        self.patch = version.patch

def SDL_VERSION(version):
    return _SDL_version
