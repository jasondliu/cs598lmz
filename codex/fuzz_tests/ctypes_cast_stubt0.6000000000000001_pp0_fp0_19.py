import ctypes
ctypes.cast(0, ctypes.py_object)

import ctypes
ctypes.cast(0, ctypes.py_object).value

import ctypes
ctypes.pythonapi.PyFile_AsFile.argtypes = [ctypes.py_object]
ctypes.pythonapi.PyFile_AsFile.restype = ctypes.POINTER(FILE)

import ctypes
ctypes.pythonapi.PyFile_AsFile.argtypes = [ctypes.py_object]
ctypes.pythonapi.PyFile_AsFile.restype = ctypes.POINTER(FILE)
ctypes.pythonapi.PyFile_AsFile(ctypes.py_object(sys.stdin))

import ctypes
ctypes.pythonapi.PyFile_AsFile.argtypes = [ctypes.py_object]
ctypes.pythonapi.PyFile_AsFile.restype = ctypes.POINTER(FILE)
ctypes.pythonapi.PyFile_AsFile(ctypes.py_object(sys.stdin)).contents

import ctypes
ctypes.pythonapi.PyFile
