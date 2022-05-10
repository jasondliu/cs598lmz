import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)

def _getter(func):
    """
    This is a decorator for ctypes functions which converts them to properties.
    """
    return property(func)

def _setter(func):
    """
    This is a decorator for ctypes functions which converts them to properties.
    """
    return property(None, func)

# class _lib(object):
#     """
#     This is a proxy for the ctypes library.
#     """
#     def __init__(self, lib):
#         self._lib = lib

#     def __getattr__(self, name):
#         try:
#             return getattr(self._lib, name)
#         except AttributeError:
#             return getattr(self._lib, name + "_")

#     def __setattr__(self, name, value):
#         if name.startswith("_"):
#             super(_lib, self).__setattr__(
