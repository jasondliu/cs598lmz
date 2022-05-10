import ctypes
ctypes.cast(123, ctypes.py_object)

ctypes.pythonapi.PyFile_Type.to_object
print(ctypes.pythonapi.PyFile_Type.to_object)
f = open('tmp', 'w')
print(f)
#ctypes.pythonapi.PyFile_AsFile.restype = ctypes.c_void_p
#print(ctypes.pythonapi.PyFile_AsFile(f))
print(ctypes.pythonapi.PyFile_AsFile(ctypes.py_object(f)))

def callback(arg):
    print('called back with', arg)
    #ctypes.pythonapi.PyFile_AsFile.argtypes = (ctypes.py_object,)
    #ctypes.pythonapi.PyFile_AsFile.restype = ctypes.c_void_p
    #ctypes.pythonapi.PyFile_AsFile.errcheck = lambda x: None
    print(ctypes.pythonapi.PyFile_AsFile(ctypes.py_object(arg)))
    ctypes.pythonapi.PyFile_SetBuf
