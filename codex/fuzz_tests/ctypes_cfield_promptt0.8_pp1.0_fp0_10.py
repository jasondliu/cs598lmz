import ctypes
# Test ctypes.CField
class POINT(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

class RECT(ctypes.Structure):
    pass
RECT._fields_ = [('left', ctypes.c_int),
                ('top', ctypes.c_int),
                ('right', ctypes.c_int),
                ('bottom', ctypes.c_int)]

def PointInRect(p, r):
    print p.x, p.y, r.left, r.top, r.right, r.bottom
    return (
        p.x >= r.left and
        p.x < r.right and
        p.y >= r.top and
        p.y < r.bottom)

p = POINT(0, 0)
r = RECT(0, 0, 10, 10)
print PointInRect(p, r)

r.left = -1
r.right = 5
r.top = -1
r.bottom = 5
print PointInRect
