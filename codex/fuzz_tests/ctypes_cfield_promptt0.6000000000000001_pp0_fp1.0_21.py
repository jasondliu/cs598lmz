import ctypes
# Test ctypes.CField
assert issubclass(ctypes.CField, ctypes.Array)
assert not issubclass(ctypes.CField, ctypes.Structure)
assert not issubclass(ctypes.CField, ctypes.Union)
assert not issubclass(ctypes.CField, ctypes.PyCPointerType)
assert not issubclass(ctypes.CField, ctypes.PyCArrayType)
assert not issubclass(ctypes.CField, ctypes.PyCStructType)
assert not issubclass(ctypes.CField, ctypes.PyCUnionType)
assert not issubclass(ctypes.CField, ctypes.CFuncPtr)
assert not issubclass(ctypes.CField, ctypes.CField)
assert not issubclass(ctypes.CField, ctypes.CData)
assert not issubclass(ctypes.CField, ctypes.PyCData)
assert not issubclass(ctypes.CField, ctypes.PyCArgObject)
assert not issubclass(ctypes.CField, ctypes.PyC
