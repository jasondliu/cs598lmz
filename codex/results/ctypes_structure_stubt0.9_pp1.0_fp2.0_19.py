import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    _fields_ = [('x', ctypes.c_int)]
</code>
This gives the error:
<code>(Pdb) python crash.py
  File "crash.py", line 1
    class S(ctypes.Structure):
      ^
SyntaxError: invalid syntax
</code>
while
<code>(Pdb) python crash.py
&gt; crash.py(2)&lt;module&gt;()
-&gt; class S(ctypes.Structure):
(Pdb) s
&gt; crash.py(3)&lt;module&gt;()
-&gt; x = ctypes.c_int
</code>
crashes when you step into the next line by typing "s".
Has anyone seen this before and know what's going on?  Can this be solved by compiling Python with a different flag or something?


A:

Wow, I didn't expect such a quick response!
I've set a thread up here on a post with the same problem: c.l.py.
After playing around with the debugger
