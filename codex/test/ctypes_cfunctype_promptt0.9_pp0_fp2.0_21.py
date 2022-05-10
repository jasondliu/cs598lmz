import ctypes
# Test ctypes.CFUNCTYPE to test ctypes callback support.
# See http://aaugustin.github.io/websockets/2015/07/17/python-websockets-5.html 
# and https://github.com/aaugustin/websockets/issues/191
#
# For other types, see https://mariosemes.gitbooks.io/tcl-c-interface-guide/content/type_conversion_tables.html
# and https://docs.python.org/3.5/library/ctypes.html#ctypes.c_void_p
functype = ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.c_int32)
#def callback(s, i):
#  ret = int(s) and i
#  print('callback({}, {}) = {}, {}'.format(s, i, ret, not ret))
#  return ret and i
#callbackall = functype(callback)



# Import Tcl from shared library
