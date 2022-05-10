import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong
    y = ctypes.c_short

def f(x, y, z):
    # print(x,y,z)
    i = z
    y.x = x
    y.y = i
    a = y.y
    if a > 5:
        print('a too big')
        print(y.x)
        print(a)
    return a 
def g():
    X = S()
    a = f(4, X, 5)
    return a

g()
