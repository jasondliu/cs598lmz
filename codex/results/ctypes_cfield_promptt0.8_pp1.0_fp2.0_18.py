import ctypes
# Test ctypes.CField
try:
    ctypes.CField(ctypes.c_char, 'name')
    have_CField = True
except AttributeError:
    have_CField = False

# Test ctypes.SimpleType
try:
    ctypes.SimpleType(ctypes.c_char)
    have_SimpleType = True
except AttributeError:
    have_SimpleType = False

# Test ctypes.PyCParser
try:
    ctypes.PyCParser.CParser
    have_CParser = True
except AttributeError:
    have_CParser = False

# Test ctypes.CThunkObject
try:
    ctypes.CThunkObject.__call__
    have_CThunkObject = True
except AttributeError:
    have_CThunkObject = False

# Test ctypes.Array
try:
    ctypes.Array(1)
    have_Array = True
except TypeError:
    have_Array = False

# Test ctypes.POINTER
try:
    ctypes.POINTER(1)
    have_
