import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    _fields_ = [
        ('a', x, 2),
        ('b', y, 1),
    ]
</code>
Which gives me <code>ValueError: Implicit bitfield size must be specified.</code> I can't figure out how to specify the field size without explicitly instantiating the field.


A:

If I understand the question correctly, this is one way to do it:
<code>In [2]: class S(ctypes.Structure):
   ...:     _fields_ = [
   ...:         ('a', ctypes.c_int, 2),
   ...:         ('b', ctypes.c_int, 1),
   ...:     ]
   ...:     
   ...:     

In [3]: S
Out[3]: __main__.S

In [4]: S._fields_
Out[4]: (('a', c_long, 2), ('b', c_long, 1))
</code>

