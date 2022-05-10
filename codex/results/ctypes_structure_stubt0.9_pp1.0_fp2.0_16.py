import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int.in_dll(kernel32, 'x')
    y = ctypes.c_int.in_dll(kernel32, 'y')
    z = ctypes.c_int.in_dll(kernel32, 'z')
    text = ctypes.c_wchar_p.in_dll(kernel32, 'text')
