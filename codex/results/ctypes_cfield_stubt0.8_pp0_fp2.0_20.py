import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
</code>
In Python 2.7:
<code>&gt;&gt;&gt; S.x.__class__
_ctypes.CField
</code>
In Python 3.5:
<code>&gt;&gt;&gt; S.x.__class__
_ctypes.CField
</code>
In Jython 2.7 (using ctypes from PyPI):
<code>&gt;&gt;&gt; S.x.__class__
&lt;type '_ctypes.CField'&gt;
</code>
In Jython 2.7 (using ctypes from PyPy-C):
<code>&gt;&gt;&gt; S.x.__class__
org.python.modules.cpyext.ctypes.CField
</code>

