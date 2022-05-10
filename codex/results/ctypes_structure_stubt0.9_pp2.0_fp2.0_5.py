import ctypes

class S(ctypes.Structure):
    x = 3
</code>
The output here (<code>pdb.pm()</code> in my example) looks good. Notice that the class is flagged as a "structure" in the <code>__class__</code> listing:
<code>&gt;&gt;&gt; pdb.pm()
-&gt; class S(ctypes.Structure):
(Pdb) b
Breakpoint 1 at &lt;string&gt;:1
(Pdb) c
&gt; &lt;string&gt;(1)&lt;module&gt;()
(Pdb) l
  1  -&gt; class S(ctypes.Structure):
  2      x = 3
  3
  4
(Pdb) p S.__class__
out&gt; ctypes.Structure
</code>
The error
However, here's a case where I'd run into problems:
<code>&gt;&gt;&gt; class S(ctypes.Structure):
...     pass
...
&gt;&gt;&gt; class T(S):
...
