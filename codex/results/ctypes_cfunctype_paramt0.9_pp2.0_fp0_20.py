import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

class BindingException(Exception):
    pass

def findCallback(funcname):
    funcname += '_callback'
    try:
        return getattr(rtffine, funcname)
    except (AttributeError, NameError):
        raise BindingException(funcname + " not found")

def createCallback(funcname, argtype, *args):
    funcname += '_callback'
    try:
        ccallback = getattr(rtffine, funcname)
    except (AttributeError, NameError):
        raise BindingException(funcname + " not found")
    return FUNTYPE((argtype,))(ccallback(*args))

################################################################################
# log functions
################################################################################

rtffine.log_set_level.argtypes = [ctypes.c_int,]
rtffine.log_get_level.argtypes = []
rtffine.log_get_level.restype = ctypes.c_int

LOG_ERROR = 0
LOG_WARN = 1
LOG_INFO = 2
LOG_DEBUG = 3
LOG_TR
