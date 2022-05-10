import ctypes
ctypes.cast((2, ctypes.py_object(55)))
type(ctypes.cast((2, ctypes.py_object(55))))
a=ctypes.cast((2, ctypes.py_object(55)), ctypes.py_object).value
a[0]
a[1]
dir(ctypes)
dir()
dir(type)
 int('0b0',2)
 int('0b1',2)
 int('0b10',2)
 int('0b01',2)
 len(ctypes.cast((1,3), ctypes.py_object).value)
len(ctypes.cast((1,3), ctypes.py_object).value, 2)
a=ctypes.cast((1, 2, 3, 4, 5, 6), ctypes.py_object).value
a
a[2]
b=a[2]
b[1]
a=ctypes.cast((1, 2, 3, 4, 5, 6), ctypes.py_object).value
b=a[2]
b[2]
a=ctypes.cast
