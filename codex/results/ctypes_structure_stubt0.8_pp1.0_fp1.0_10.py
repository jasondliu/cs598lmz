import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)
    y = ctypes.c_int(2)

s = S()
print(s.x, s.y)
s.x = ctypes.c_int(5)
print(s.x, s.y)
</code>


A:

From the documentation (https://docs.python.org/3.8/library/ctypes.html?highlight=c%20types#setting-instance-variables): 
<blockquote>
<p>Setting instance variables to values of the wrong type raises ValueError.</p>
</blockquote>
And since <code>5</code> is not a valid <code>ctypes.c_int</code> object, <code>ValueError</code> is raised.

