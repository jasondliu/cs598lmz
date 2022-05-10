import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    _fields_ = [
        ('y', ctypes.c_float),
        ('z', ctypes.c_float),
        ('x', ctypes.c_float),
    ]
print S.__dict__
print S.__dict__['x'] is ctypes.c_float
</code>
When run, this emits:
<code>{'_fields_': [('y', &lt;class 'ctypes.c_float'&gt;), ('z', &lt;class 'ctypes.c_float'&gt;), ('x', &lt;class 'ctypes.c_float'&gt;)], '_pack_': 1, '__doc__': None, '__module__': '__main__', 'x': &lt;class 'ctypes.c_float'&gt;}
True
</code>
which is what I'd expect. You could also just use <code>setattr(S, 'x', ctypes.c_float)</code>, or replace the entire <code>_fields_</code> tuple.

