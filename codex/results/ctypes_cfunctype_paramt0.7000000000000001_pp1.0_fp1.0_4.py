import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int,ctypes.c_int)

def test(a,b):
    print a,b
    return a+b


ctypes.pythonapi.Py_InitModule4.argtypes = [ctypes.c_char_p,ctypes.py_object,ctypes.c_char_p,ctypes.py_object,ctypes.c_int]
ctypes.pythonapi.Py_InitModule4(ctypes.c_char_p(modname),methods,doc,None,1)

#ctypes.pythonapi.Py_InitModule4_64(ctypes.c_char_p(modname),methods,doc,None,1)
