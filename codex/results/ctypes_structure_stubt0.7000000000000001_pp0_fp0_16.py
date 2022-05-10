import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint8
    def __init__(self, *args, **kwargs):
        super(S, self).__init__(*args, **kwargs)
        print(self)

print(S.__new__(S))
</code>
prints (on Python 2.7):
<code>&lt;__main__.S object at 0x10a0ed3e0&gt;
&lt;__main__.S object at 0x10a0ed3f0&gt;
</code>
while
<code>ctypes.Structure.__new__(S)
</code>
prints
<code>&lt;__main__.S object at 0x10a0ed3e0&gt;
</code>

The first print is the default <code>__new__(cls, *args, **kwargs)</code> implementation of <code>object</code>:
<code>&gt;&gt;&gt; object.__new__
&lt;built-in method __new__ of type object at 0x7fb5f37
