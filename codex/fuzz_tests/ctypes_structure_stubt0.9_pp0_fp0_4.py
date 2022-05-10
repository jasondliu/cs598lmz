import ctypes

class S(ctypes.Structure):
    x = (ctypes.c_bool * 200)()

s = S()
print s.x
print len(s.x)
</code>
(on CPython 2.7.6, ctypes 1.1.0 with g++ 4.8.2)

