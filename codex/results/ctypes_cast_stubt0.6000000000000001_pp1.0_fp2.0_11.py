import ctypes
ctypes.cast(1, ctypes.py_object)

# Call a function
ctypes.pythonapi.PyFile_AsFile.restype = ctypes.POINTER(FILE)
ctypes.pythonapi.PyFile_AsFile.argtypes = [py_object]
file_ptr = ctypes.pythonapi.PyFile_AsFile(py_object(sys.stdout))
file_ptr.contents

# Convert ctypes instance to a Python object
ctypes.pythonapi.PyCObject_AsVoidPtr.restype = ctypes.c_void_p
ctypes.pythonapi.PyCObject_AsVoidPtr.argtypes = [py_object]
ctypes.pythonapi.PyCObject_AsVoidPtr(py_object(c_void_p(id(object))))

# Call a function
ctypes.pythonapi.PyCObject_FromVoidPtr.restype = py_object
ctypes.pythonapi.PyCObject_FromVoidPtr.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
ctypes.
