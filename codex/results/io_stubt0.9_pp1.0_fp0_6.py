import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
a = []
del view
for i in range(10):
    a.append(i)

def zap():
    for i in range(10):
        del a[i]

zap()
del zap
t = 5
while t:
    print a
    if t == 2:
        a = []
        a = None
    t -= 1
del t

a = [0] * 3
a[2] = 6
del a

def y():
    a = []
    a.append(1)
    print a
    del a

def x(i):
    a = []
    a.append(i)
    del a

def w():
    return 1

for i in range(10):
    j = w()
    x(i)
if w() == 1:
    y()
