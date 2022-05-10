import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CFuncPtr(ctypes.CFuncPtr):
    def _get_check_retval_(self, *args):
        return 0

ctypes.CFuncPtr.__name__ = "CFuncPtr"

def f(x):
    return x + 1


def f_no_annot(x):
    return x + 1

def f_no_annot_no_return(x):
    return x + 1

def f_no_annot_no_param(x):
    return x + 1

def f_no_annot_no_return_no_param(x):
    return x + 1

def f_no_annot_no_param_no_return(x):
    return x + 1

def f_no_annot_no_return_no_param(x):
    return x + 1

def f_no_annot_no_param_no_return_no_param(x):
    return x + 1

def f_no_annot_no_return_no_param_no_param(x):
    return x
