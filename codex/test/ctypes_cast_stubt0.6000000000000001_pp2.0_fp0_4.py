import ctypes
ctypes.cast(0, ctypes.py_object)

#
#
#
#class Foo:
#    def __init__(self, x):
#        self.x = x
#
#
#foo = Foo(1)
#
#
#def func():
#    pass
#
#
#print(ctypes.pythonapi.PyCapsule_GetPointer.restype)
#print(ctypes.pythonapi.PyCapsule_GetPointer.argtypes)
#
#py_object_p = ctypes.pythonapi.PyCapsule_GetPointer(ctypes.py_object(foo), None)
#print(py_object_p)
#print(ctypes.cast(py_object_p, ctypes.py_object).value)
#
#py_object_p = ctypes.pythonapi.PyCapsule_GetPointer(ctypes.py_object(func), None)
#print(py_object_p)
#print(ctypes.cast(py_object_p, ctypes.py_object).value)

