import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()

s = S()
print(s.x)
s.x = 1
print(s.x)

s.x = 'abc'
print(s.x)
</code>
Output:
<code>0
1
Traceback (most recent call last):
  File "C:\Users\paul\Documents\Programming\Python\test.py", line 11, in &lt;module&gt;
    s.x = 'abc'
TypeError: an integer is required
</code>

