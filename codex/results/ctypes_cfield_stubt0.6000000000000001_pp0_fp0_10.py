import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

try:
    raise TypeError
except TypeError:
    tb = sys.exc_info()[2]

while tb:
    tb = tb.tb_next

S()
