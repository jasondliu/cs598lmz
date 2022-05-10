import ctypes
# Test ctypes.CField
print('Size of CFunctions object :', ctypes.sizeof(ctypes.CFunctionType))
print('Size of CField object     :', ctypes.sizeof(ctypes.CField))

# It seems anything can be a field. Lets test that.

# Test if ctypes.CFuncPtr can be used as a field.
print('Size of CFuncPtr object :', ctypes.sizeof(ctypes.CFuncPtr))
class TestCFuncPtr(ctypes.LittleEndianStructure):
    _fields_ = [('ptr', ctypes.CFuncPtr)]
print('Size of TestCFuncPtr object :', ctypes.sizeof(TestCFuncPtr))
print('Size of hte object :', ctypes.sizeof(TestCFuncPtr(ctypes.CFuncPtr(None))))
# Test if ctypes.Structure can be used as a field.
print('Size of Structure object :', ctypes.sizeof(ctypes.Structure))
class TestStruct(ctypes.LittleEndianStructure):
    _fields_ = [('ptr', ctypes.Structure)]
