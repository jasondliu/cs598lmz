import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
	def myfun():
		print "myfun"
	return myfun
print fun()

# c = ctypes.pythonapi
# print c
# print c.PyString_AsString.argtypes
# print ctypes.c_char_p
# fun = ctypes.pythonapi.PyString_AsString
# print fun
# fun.restype = ctypes.c_char_p
# print fun('hhh')

import ctypes, sys, os
# print ctypes.c_int.in_dll(ctypes.pyapi.python, '_is_pyc_file')
# print ctypes.c_int.in_dll(ctypes.pyapi.python, '_is_pyc_file').value
fun = ctypes.pythonapi.PyString_AsString
print fun

c = ctypes.CDLL(os.path.join(sys.exec_prefix, 'lib', 'libpython2.7.so.1.0'))
print c

# def pymain(argc, argv):
#     # This code mostly matches the
