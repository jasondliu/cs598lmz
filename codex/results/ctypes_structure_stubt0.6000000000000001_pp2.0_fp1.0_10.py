import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_float

def F(S):
    return S.x * S.y

print F(S(5, 3.5))
</code>
I get the following error:
<code>---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
&lt;ipython-input-1-1e2acf5b14c3&gt; in &lt;module&gt;()
      4 class S(ctypes.Structure):
      5     x = ctypes.c_int
----&gt; 6     y = ctypes.c_float
      7 
      8 def F(S):

TypeError: __init__() takes at least 2 arguments (1 given)
</code>
If I remove the <code>y</code> field, or "comment it out" by preceding it with <code>#</code>, I get the correct answer. Can anyone tell me what I'm doing wrong?


A:

Your problem is that the first argument to a <code>ctypes.Structure</code>
