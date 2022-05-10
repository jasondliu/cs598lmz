import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_int

print S.x
print S.y
</code>
But this fails:
<code>import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_double),
                ('y', ctypes.c_int)]

print S.x
print S.y
</code>
I get an error:
<code>AttributeError: type object 'S' has no attribute 'x'
</code>
I would like to use the _fields_ syntax because I have a more complex structure, with nested structures.
Is there a way to do this?
Thank you!


A:

<code>_fields_</code> is a class variable, not an instance variable, so you access it as <code>S._fields_</code>.  If you want to get the names of the fields, you can do it like this (but you probably want to use <code>setattr()</code> instead of <code>__setattr__()</code>):
<code>&
