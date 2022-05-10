import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]
    _anonymous_ = ["a"]
X._fields_

# Test ctypes.PyCFuncPtr
ctypes.CFUNCTYPE(ctypes.c_int)

# Test ctypes.CArgObject
ctypes.CArgObject

# Test ctypes.CThunkObject
ctypes.CThunkObject

# Test ctypes.CDLL
ctypes.CDLL

# Test ctypes.PyDLL
ctypes.PyDLL

# Test ctypes.LibraryLoader
ctypes.LibraryLoader

# Test ctypes.PyObj_FromPtr
ctypes.PyObj_FromPtr

# Test ctypes.PyCObject_FromVoidPtr
ctypes.PyCObject_FromVoidPtr

# Test ctypes.PyCObject_AsVoidPtr
ctypes.PyCObject_AsVoidPtr

# Test ctypes.PyCObject_Import
ctypes.PyCObject_Import

# Test ctypes.
