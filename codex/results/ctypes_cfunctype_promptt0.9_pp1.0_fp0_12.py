import ctypes
# Test ctypes.CFUNCTYPE
# Uncomment following line to easily show the tp_mro of CFUNCTYPE
# CFUNCTYPE.__mro__

class P: pass
class C(P): pass
class D(P): pass
class E(C, D): pass

print(E.__mro__)

PyType_Type.tp_mro.offset
# Test for Py_TYPE(obj)->tp_mro
# These comment lines will help you to identify the meaning of tp_mro in C source code
# From include/object.h
# 'typedef struct _typeobject PyTypeObject;'
# 'struct _typeobject {
#	PyObject_VAR_HEAD
# 	const char *tp_name;
#	...
#	PyObject *(*tp_mro_concrete)(PyTypeObject *, PyObject *);
#	PyObject *tp_mro;
#	...
#	};'

# From Objects/typeobject.c :
# 'static PyObject *
# mro_internal(PyTypeObject *type, Py
