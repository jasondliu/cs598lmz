import ctypes
ctypes.cast(1, ctypes.py_object)

# pypy
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: cannot cast an address to a pointer
'''
