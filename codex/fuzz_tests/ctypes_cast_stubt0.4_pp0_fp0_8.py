import ctypes
ctypes.cast(0, ctypes.py_object)

# SEGV
import _ctypes
_ctypes.PyObj_FromPtr(0)

# SEGV
import ctypes
ctypes.pythonapi.PyCObject_FromVoidPtrAndDesc(0, 0, 0)

# SEGV
import ctypes
ctypes.pythonapi.PyCObject_AsVoidPtr(0)

# SEGV
import ctypes
ctypes.pythonapi.PyCObject_Import(0, 0)

# SEGV
import ctypes
ctypes.pythonapi.PyCObject_SetVoidPtr(0, 0)

# SEGV
import ctypes
ctypes.pythonapi.PyCObject_Type.tp_dealloc(0)

# SEGV
import ctypes
ctypes.pythonapi.PyCObject_Type.tp_getattro(0, 0)

# SEGV
import ctypes
ctypes.pythonapi.PyCObject_Type.tp_setattro(0, 0, 0)

# SEG
