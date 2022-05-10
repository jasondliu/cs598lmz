import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.py_object)
PYFUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
#
def funA(data):
    print "funA:",data, type(data)
def funA_PYFUN(data):
    print "funA_PYFUN:",data, type(data)
    return data

funP = FUNTYPE(funA)  # call the c function pointer
funP_PYFUN = PYFUNTYPE(funA_PYFUN)  # call the c function pointer

# data_from_c  = "from c -> pyrun"
# funP(data_from_c)
# ret_from_py  = "from py -> c"
# data_r       = callfunc(funP_PYFUN, ret_from_py)
# print data_r

if sys.platform == "win32":
    libname = "libso"
    func_name = "EXPORT_CALL_PY"
    func_name_py
