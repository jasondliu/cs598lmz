import ctypes

class S(ctypes.Structure):
    x = ctypes.c_short

s = S()
print(s.x)
s.x = 2
print(s.x)

s.x = -5
print(s.x)
s.x = 2**15-1
print(s.x)
s.x = -2**15
print(s.x)
</code>
Interestingly, in Python 3.5.1, it prints:
<code>0
2
-5
32767
-32767
</code>
While in Python 3.6.0, it prints:
<code>0
2
-5
32767
-32768
</code>
This might be a bug in Python 3.5.1.

