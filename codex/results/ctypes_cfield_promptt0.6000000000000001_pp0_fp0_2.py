import ctypes
# Test ctypes.CField

class POINT(ctypes.Structure):
    pass

class RECT(ctypes.Structure):
    _fields_ = [("left", ctypes.c_long),
                ("top", ctypes.c_long),
                ("right", ctypes.c_long),
                ("bottom", ctypes.c_long)]

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long),
                ("y", ctypes.c_long)]

def test(name, value, expected):
    # print('%s: %r == %r' % (name, value, expected))
    assert value == expected

test('RECT.left', RECT().left, 0)
test('RECT.right', RECT().right, 0)
test('RECT.top', RECT().top, 0)
test('RECT.bottom', RECT().bottom, 0)

r = RECT()
r.left = 10
r.top = 20
r.right = 30
r.bottom = 40

test('r.left',
