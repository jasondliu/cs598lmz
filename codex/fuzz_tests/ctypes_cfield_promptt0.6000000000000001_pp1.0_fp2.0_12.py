import ctypes
# Test ctypes.CField
# <http://starship.python.net/crew/theller/ctypes/tutorial.html>

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long),
                ("y", ctypes.c_long)]

class RECT(ctypes.Structure):
    _fields_ = [("left", ctypes.c_long),
                ("top", ctypes.c_long),
                ("right", ctypes.c_long),
                ("bottom", ctypes.c_long)]

class WINDOWPOS(ctypes.Structure):
    _fields_ = [("hwnd", ctypes.c_void_p),
                ("hwndInsertAfter", ctypes.c_void_p),
                ("x", ctypes.c_int),
                ("y", ctypes.c_int),
                ("cx", ctypes.c_int),
                ("cy", ctypes.c_int),
                ("flags", ctypes.c_uint)]

class NMHDR(ctypes.Structure):
