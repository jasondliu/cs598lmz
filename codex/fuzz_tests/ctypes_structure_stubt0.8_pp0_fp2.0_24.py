import ctypes

class S(ctypes.Structure):
    x = (1, 2)
</code>
but this causes a syntax error (class definitions may not contain tuple parameters).  I tried using
<code>class S(ctypes.Structure):
    _fields_ = [("x", (1, 2))]
</code>
but that causes a segfault.
Is it possible to use a tuple for a ctypes struct field?  How?


A:

I have a similar problem. I have a structure that looks like this:
<code>class HLA_BASIC_ATTRIBUTE_INFO(Structure):
    _fields_ = [('class_name', c_char*255),
                ('name', c_char*255),
                ('name_length', c_ushort),
                ('data_type', c_ushort),
                ('order', c_ushort),
                ('transportation', c_ushort),
                ('dimension', c_ushort),
                ('sharerable', c_ushort),
                ('update_type', c_ushort),
                ('update_condition', c_ushort),
               
