import ctypes
# Test ctypes.CFUNCTYPE
if (os.name == 'nt'):
    ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
else:
    ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
# Test ctypes.POINTER(ctypes.c_int)
ctypes.POINTER(ctypes.c_int)
# Test ctypes.pythonapi
ctypes.pythonapi
# Test ctypes.pythonapi.PyFile_AsFile
ctypes.pythonapi.PyFile_AsFile
# Test ctypes.pythonapi.PyFile_AsFile.argtypes
ctypes.pythonapi.PyFile_AsFile.argtypes
# Test ctypes.pythonapi.PyFile_AsFile.restype
ctypes.pythonapi.PyFile_AsFile.restype
# Test ctypes.pythonapi.PyFile_AsFile.__doc__
ctypes.pythonapi.PyFile_AsFile.__doc__
# Test ctypes.pythonapi.PyFile_AsFile.__
