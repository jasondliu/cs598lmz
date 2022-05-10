import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double

print ctypes.sizeof(S)
</code>
I get an error
<blockquote>
<p>python test.py<br/>
  Traceback (most recent call last):
    File "test.py", line 6, in 
      print ctypes.sizeof(S)
  TypeError: size of type 'class test.S' is not defined</p>
</blockquote>
Why is this and how do I fix it?


A:

What you want is:
<code>print ctypes.sizeof(S.x)
</code>
This prints <code>8</code> on my system. 
Or, if you want the size of the whole structure (i.e. <code>sizeof(S.x) + alignment(S.x)</code>):
<code>print ctypes.sizeof(S)
</code>

