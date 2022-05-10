import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.c_void_p, ctypes.c_void_p)

def load_library(libname):
    """ Load a ctypes library in a platform-independent way """
    import platform
    import os

    if platform.system() == "Windows" and not libname.endswith('.dll'):
        libname += '.dll'
    elif platform.system() == "Linux" and not libname.endswith('.so'):
        libname = 'lib' + libname + '.so'
    elif platform.system() == "Darwin" and not libname.endswith('.dylib'):
        libname = 'lib' + libname + '.dylib'

    libdir = os.path.dirname(__file__)
    libpath = os.path.join(libdir, libname)
    try:
        return ctypes.cdll.LoadLibrary(libpath)
    except:
        raise ImportError('Could not load ' + libname)

_lib = load_library('cbits')

