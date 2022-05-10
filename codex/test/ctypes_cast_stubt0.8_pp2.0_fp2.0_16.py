import ctypes
ctypes.cast(None, ctypes.py_object)
a = 1
a
a += 1
a
 
l = []
l.append(None)
l
l[0]
 
def f(x):
    if x >= 0:
        return 1
    else:
        return None
 
f(1)
f(-1)
bool(f(1))
bool(f(-1))
 
b = bool(f(1))
b
l = []
l.append(f(1))
l
l.append(f(-1))
l
l[0]
l[1]
bool(l[0])
bool(l[1])
 
for v in l:
    print(bool(v))
def g(x, y):
    if x >= y:
        return x
    else:
        return y
 
a = g(3, 5)
a
a = g(5, 3)
a
a = g(5, 5)
a
