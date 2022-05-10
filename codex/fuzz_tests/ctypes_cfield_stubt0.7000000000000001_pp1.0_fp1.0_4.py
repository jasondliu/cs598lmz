import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def callback(x):
    print('callback:', x)
    return 42

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(callback)

class D(ctypes.c_object):
    _fields_ = [('x', ctypes.c_int),
                ('callback', ctypes.CField),
                ('callback2', ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int))]

d = D()
d.callback = CALLBACK
d.callback2 = CALLBACK

print(d.callback2(99))
print(d.callback(99))
print(d.callback2(99))
print(d.callback(99))
try:
    print(d.callback3(99))
except AttributeError:
    pass
