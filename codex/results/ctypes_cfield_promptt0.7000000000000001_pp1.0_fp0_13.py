import ctypes
# Test ctypes.CField_Union

class Union1(ctypes.Union):
    _fields_ = [
        ('a', ctypes.c_int),
        ('b', ctypes.c_int)
    ]
    _anonymous_ = ('t',)

Union1._fields_ = [
    ('t', Union1)
]

class Union2(ctypes.Union):
    _fields_ = [
        ('a', ctypes.c_int),
        ('b', ctypes.c_int)
    ]
    _anonymous_ = ('t',)

Union2._fields_ = [
    ('t', Union2),
    ('c', ctypes.c_int)
]

class Union3(ctypes.Union):
    _fields_ = [
        ('a', ctypes.c_int),
        ('b', ctypes.c_int)
    ]
    _anonymous_ = ('t',)

Union3._fields_ = [
    ('t', Union3),
    ('c', ctypes.c_int),
    ('d', ctypes
