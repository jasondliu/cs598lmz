import ctypes
ctypes.cast(id(0), ctypes.py_object).value = 'JABBERWOCKY'
print ('')
