import ctypes
# Test ctypes.CField
print('Test struct/union field:')

class POINT(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]
class RECT(ctypes.Structure):
    _fields_ = [('topleft', POINT),
                ('bottomright', POINT)]
class BOX(ctypes.Structure):
    _fields_ = [('rightside', ctypes.c_int),
                ('leftside', ctypes.c_int)]

class BAR(ctypes.Union):
    _fields_ = [('box', BOX),
                ('rectangle', RECT),
                ('left', ctypes.c_int),
                ('right', ctypes.c_int)]

pt1 = POINT(1, 2)
pt2 = POINT(3, 4)
rect = RECT(pt1, pt2)
bar = BAR()
bar.rectangle = rect
print(bar.box.rightside)

try:
    bar.box.rectangle = rect
except Type
