import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

inst_fld_addrs = [id(x) for x in [S().x, S().x]]

class_fld_addrs = [id(S.x), id(S.x)]

print inst_fld_addrs
print class_fld_addrs

# Verify that x + y does not read y.x
class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

def fn(a, b):
    a.x = 1
    a.y = 2
    b.x = 3
    b.y = 4
    return a.x + b.x

s = S()
r = fn(s, s)
print r

s = S()
r = fn(s, s)
print r

# Verify that x += y does not read y.x
s = S()
s.x = 1
s.y = 2
s.x += s.y
print s.x

# Verify that x
