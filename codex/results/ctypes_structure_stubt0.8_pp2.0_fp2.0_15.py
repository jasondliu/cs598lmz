import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

print(S.x.offset)
print(S.y.offset)
</code>
Here's the output:
<code>&gt;&gt;&gt; python3 test.py
0
4
&gt;&gt;&gt;
</code>
As seen above, the offset of <code>y</code> is 4. This is the default alignment of int in my system.
But the problem is that we cannot modify the alignment of the structure:
<code>&gt;&gt;&gt; S.x.aligned = 1
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
AttributeError: readonly attribute 'aligned'
</code>
So the question is: How can we modify the alignment of individual field of the structure without changing overall alignment of the structure?


A:

This is not possible. You can either accept the default alignment or change all field alignments.

