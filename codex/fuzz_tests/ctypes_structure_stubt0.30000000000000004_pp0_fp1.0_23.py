import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()

s.x = 1
s.y = 2

print s.x
print s.y
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "C:/Users/Dmitry/Desktop/test.py", line 10, in &lt;module&gt;
    s.x = 1
AttributeError: 'S' object has no attribute 'x'
</code>
Why?


A:

You need to create an instance of the class first:
<code>s = S()
</code>

