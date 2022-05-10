import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print(s.x, s.y)

cs = S.in_dll(ctypes.cdll.msvcrt, "s")

print(cs.x, cs.y)

cs.x = 3
cs.y = 4

print(cs.x, cs.y)
print(s.x, s.y)

"""
>>> python test.py
1 2
2 3
3 4
1 2
"""
