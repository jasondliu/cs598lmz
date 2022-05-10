import ctypes
ctypes.cast(0, ctypes.py_object).value

# See http://docs.python.org/dev/c-api/object.html#c.PyObject_FromVoidPtr

#>>> import ctypes
#>>> ctypes.cast(0, ctypes.py_object).value
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  File "/usr/lib/python2.7/ctypes/__init__.py", line 356, in getattr
#    func = self.__getitem__(name)
#  File "/usr/lib/python2.7/ctypes/__init__.py", line 361, in __getitem__
#    func = self._FuncPtr((name_or_ordinal, self))
#ctypes.ArgumentError: argument 1: <type 'exceptions.TypeError'>: expected LP_FuncPtr instance instead of int
#>>> ctypes.cast(0, ctypes.py_object).value
#Traceback (most recent call last):
#  File "<stdin
