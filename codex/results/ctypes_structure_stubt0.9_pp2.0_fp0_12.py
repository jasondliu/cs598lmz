import ctypes

class S(ctypes.Structure):
    x = []

s = S()
print(repr(s))
</code>
Here, I get:
<code>Traceback (most recent call last):
  File "test.py", line 5, in &lt;module&gt;
    s = S()
  File "/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/ctypes/__init__.py", line 348, in __init__
    self._update(_byref(self), *args)
RuntimeError: maximum recursion depth exceeded
</code>
I can't seem to find any documentation about a limitation on the number of elements in a <code>C</code>-style array.  I feel like this should be documented somewhere, but I'm having difficulty finding anything.


A:

In the end, the answer came down to the documentation of array members in <code>ctypes</code>:
<blockquote>
<p>array (a,n)</p>
<p>The array type creates an array of n elements, each element also being of type a. Note that it is an error to use
