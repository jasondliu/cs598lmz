import ctypes

class S(ctypes.Structure):
    x = ctypes.c_float * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10 * 11 * 12 * 13 * 14 * 15 * 16 * 17 * 18 * 19 * 20 * 21 * 22 * 23 * 24 * 25 * 26 * 27 * 28 * 29 * 30 * 31 * 32 * 33 * 34 * 35 * 36 * 37 * 38 * 39 * 40 * 41 * 42 * 43 * 44 * 45 * 46 * 47 * 48 * 49 * 50 * 51 * 52 * 53 * 54 * 55 * 56 * 57 * 58 * 59 * 60 * 61 * 62 * 63 * 64

print len(S.x.__ctype_be__.fields)
print S.x.__ctype_be__.fields
print len(S.x.__ctype_le__.fields)
print S.x.__ctype_le__.fields
</code>
outputs on my machine:
<code>$ python test.py
64
{'f0': &lt;Field type=c_float, ofs=0x0, size=0x4&gt;, 'f1': &lt
