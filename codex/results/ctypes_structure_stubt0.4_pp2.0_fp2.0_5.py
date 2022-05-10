import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

s = S()
s.x = 1

print(s.x)
print(s.x.__class__)
print(s.x.__class__.__base__)
print(s.x.__class__.__base__.__base__)
</code>
Output:
<code>1
&lt;class 'int'&gt;
&lt;class 'object'&gt;
&lt;class 'object'&gt;
</code>

