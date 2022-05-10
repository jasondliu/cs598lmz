import ctypes

class S(ctypes.Structure):
    x = ctypes.c_float()
    y = ctypes.c_float()
    z = ctypes.c_float()
    w = ctypes.c_float()
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

f = open(fn1, 'r')
l = f.readline().split()
numsp = int(l[0])
numpt = int(l[1])
sp = []
for i in range(numsp):
    p = f.readline().split()
    k = S(p[0], p[1], p[2], p[3])
    sp.append(k)
pt = []
for i in range(numpt):
    p = f.readline().split()
    k = S(p[0], p[1], p[2], p[3])
    pt.append(k)
f.close()

numelem=0
si=f2.find(
