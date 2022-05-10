import ctypes
# Test ctypes.CFUNCTYPE

class X(object):
    def __init__(self, x=0):
        self.x = x

def callback(x):
    x.x = 1

X_p = ctypes.POINTER(X)
X_p_p = ctypes.POINTER(X_p)
f = ctypes.CFUNCTYPE(None, X_p)(callback)

x = X()
y = X()
pp = X_p_p(x)
pp[0] = y

f(pp)
print x.x, y.x
f(x)
print x.x, y.x

"""
0 0
1 1
"""
