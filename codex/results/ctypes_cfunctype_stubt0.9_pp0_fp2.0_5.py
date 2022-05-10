import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
  print "in sand", type(sand)
  return 7

# py_object_ptr = ctypes.py_object.in_dll(ctypes.pythonapi,'__pyx_f_5sand_fun').value
# print py_object_ptr, FUNTYPE(py_object_ptr)    
# s = sand()
# print s.__pyx_vtable__.id, hasattr(s, '__pyx_vtabptr_')
# s.fun()
