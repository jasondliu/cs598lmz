import ctypes
# Test ctypes.CField

class POINT(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

class RECT(ctypes.Structure):
    _fields_ = [('left', ctypes.c_int),
                ('top', ctypes.c_int),
                ('right', ctypes.c_int),
                ('bottom', ctypes.c_int)]

class Window(ctypes.Structure):
    _fields_ = [('rect', RECT),
                ('point', POINT)]

class WindowType(Window):
    _fields_ = [('type', ctypes.c_int)]

class WindowTypeWithParent(WindowType):
    _fields_ = [('parent', WindowType)]

class WindowTypeWithParent2(WindowTypeWithParent):
    _fields_ = [('parent2', WindowType)]

class WindowTypeWithParent3(WindowTypeWithParent2):
    _fields_ = [('parent3', WindowType)]

class WindowTypeWithParent4(WindowTypeWith
