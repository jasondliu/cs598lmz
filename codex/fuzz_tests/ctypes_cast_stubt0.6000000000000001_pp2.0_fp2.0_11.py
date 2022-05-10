import ctypes
ctypes.cast(1, ctypes.py_object)

# 
# ctypes.py_object(id(1))
# TypeError: this type has no size
# 

import ctypes
ctypes.py_object(id(1))

# 
# ctypes.pythonapi.PyFile_AsFile.argtypes = [ctypes.py_object]
# AttributeError: 'module' object has no attribute 'pythonapi'
# 

import ctypes
ctypes.pythonapi.PyFile_AsFile.argtypes = [ctypes.py_object]

# 
# ctypes.pythonapi.PyFile_AsFile(0)
# AttributeError: 'module' object has no attribute 'pythonapi'
# 

import ctypes
ctypes.pythonapi.PyFile_AsFile(0)

# 
# ctypes.pythonapi.PyFile_AsFile.restype = ctypes.POINTER(FILE)
# AttributeError: 'module' object has no attribute 'pythonapi'
# 

import ctypes
ctypes.pythonapi.
