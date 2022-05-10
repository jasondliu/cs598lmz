import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
</code>
Now, create an instance of a structure with a field, and an instance of a field:
<code>&gt;&gt;&gt; s = S()
&gt;&gt;&gt; s.x
c_int(0)
&gt;&gt;&gt; f = S.x
&gt;&gt;&gt; f
&lt;CField type 'int'&gt;
</code>
If you want to use a <code>Structure</code> class with a field named <code>x</code> as a "template" for creating new <code>Structure</code> classes, you'll need to first clone the class, then replace the field with a new instance of a field:
<code>&gt;&gt;&gt; T = type(s)
&gt;&gt;&gt; T.x = f
</code>
Now <code>T</code> is a <code>Structure</code> class with a field named <code>x</code> that you can use as a template:
<code>&gt;&
