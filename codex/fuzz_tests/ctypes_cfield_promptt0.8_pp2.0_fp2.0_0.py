import ctypes
# Test ctypes.CField
hasattr(ctypes.CField, 'in_dll')

# Test ctypes.Field
hasattr(ctypes.Field, '__getitem__')
hasattr(ctypes.Field, 'from_param')
hasattr(ctypes.Field, 'in_dll')

# Test ctypes.PyCFuncPtr
hasattr(ctypes.PyCFuncPtr, 'in_dll')
