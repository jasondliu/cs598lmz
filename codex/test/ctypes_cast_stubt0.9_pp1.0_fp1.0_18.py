import ctypes
ctypes.cast(0, ctypes.py_object)

dll = None

is32Bit = (ctypes.sizeof(ctypes.c_void_p) == 4)

if is32Bit:
    dll = ctypes.cdll.LoadLibrary("../OpenSimRoot/builds/Release/OpenSimMoko.dll")
