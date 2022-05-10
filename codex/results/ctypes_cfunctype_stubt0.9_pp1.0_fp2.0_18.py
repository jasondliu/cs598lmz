import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return u"\u00e8"
ctypes.pythonapi.PyUnicode_FromUnicode(None,ctypes.POINTER(ctypes.wintypes.WCHAR)(),0)
cchars = ctypes.POINTER(ctypes.wintypes.WCHAR)(u"\u00e8" + "a")
cchars2 = ctypes.POINTER(ctypes.wintypes.WCHAR)(u"\u00e8" + "a")
pystring = ctypes.pythonapi.PyUnicode_FromUnicode(None, cchars, 2);
