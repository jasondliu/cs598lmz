import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.CField):
    def __init__(self, *args):
        print(args)
        super().__init__(*args)

class S(ctypes.Structure):
    _fields_ = [('x', X)]

print(S.x)
</code>
Output:
<code>&lt;class '__main__.X'&gt;
('x', &lt;class '__main__.X'&gt;)
</code>
The first line is the <code>print(S.x)</code> statement. The second line is the output of the <code>__init__</code> method.
If you want to use a custom field type that has a different <code>__init__</code> method, you will need to override the <code>_ctypes_</code> attribute on the class to point to the correct metaclass.

