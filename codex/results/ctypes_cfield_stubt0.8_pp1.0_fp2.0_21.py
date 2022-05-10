import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
def p(v):
    print v

# SF bug #1415383
p(ctypes.c_wchar(u'x'))

# SF bug #1415549
p(ctypes.c_wchar_p(u"x"))

p(ctypes.c_int.from_address(id(ctypes.c_int(1))))

# SF bug #1415563
p(ctypes.c_int(ctypes.c_int(1)))

# SF bug #1415565
p(ctypes.c_int(ctypes.c_short(1)))

# SF bug #1415574
p(ctypes.c_int(ctypes.c_long(1)))

# SF bug #1415581
p(ctypes.c_long(ctypes.c_int(1)))

# SF bug #1415591
p(ctypes.c_long(ctypes.c_short(1)))

# SF bug #1415599
p(ctypes.c_long(ctypes.c_long(1)))
