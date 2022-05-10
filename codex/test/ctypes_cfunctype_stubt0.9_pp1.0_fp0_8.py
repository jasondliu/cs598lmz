import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return np.array([1,2,3])
fun()


# %%
import numpy as np
import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_void_p)
def fun(a):
    a = np.array([1,2,3])
fun()


# %%
import ctypes
import ctypes.util

def pYN(ans, default_yn="Y"):
    """
    'yes' or 'no' question.    If the user only hits 'Enter', it accepts the
    given default_yn setting.
    """

    aYN = raw_input("%s [%s]: " % (ans, default_yn))
    if aYN.strip() == "":
        return default_yn
    return aYN


def set_lib_path(libpath=None, dirname=""):
    import ctypes
    import ctypes.util
    import os
    import sys

