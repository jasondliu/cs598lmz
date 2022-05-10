import ctypes
ctypes.cast(0, ctypes.py_object)
 
# outputs <PyCObject at 0x400139f0>

def bar():
    ctypes.cast(0, ctypes.py_object)
    return 'bar'

class CpythonImplementationDetails:
    pass

# the following does not work:
