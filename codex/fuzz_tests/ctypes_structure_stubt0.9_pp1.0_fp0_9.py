import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
str(s)
s.x = 1
s.y = 1
str(s) # expected "&lt;ctypes.Structure object at 0x000000000000002...&gt;"
</code>
In <code>pandas</code> case, data object (<code>data</code>) is a nested dictionary. So, in <code>__repr__</code> recursion level is <code>0</code>, but in <code>Cols.__repr__</code> it is <code>1</code> and other levels.
What could be the reason?


A:

This is happening because the call to <code>dict.__repr__</code> in your recursive function does not return the string representation, but instead evaluates to <code>None</code>.
<code>&gt;&gt;&gt; class Obj(object):
...     def __init__(self, x):
...         self.x = x
... 
&gt;&gt;&gt; def
