import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long()
    y = ctypes.c_long()

e = ctypes.c_void_p(-1)
i = ctypes.c_long(-1)
s = S(x=ctypes.c_long(-1), y=ctypes.c_long(-1))

print(repr(s))
print('e: %s, i: %s, s: %s' % (repr(e), repr(i), repr(s)))

for _ in range(10):
    incr(e, i, s)
    print('e: %s, i: %s, s: %s' % (repr(e), repr(i), repr(s)))

'''
$ python3 test2.py
<Structure object at 0x7f59f47b00a0>
e: <cparam 'P' (-1)>, i: c_long(-1), s: <Structure object at 0x7f59f47b00a0>
e: <cparam 'P' (-1)>, i: c_
