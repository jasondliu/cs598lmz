import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class simple(ctypes.Structure):
    _fields_ = [('data',ctypes.c_int*10)]

s = simple()

for i in range(10):
    s.data[i] = i
    print (ctypes.addressof(s.data[i]))


</code>
How do I produce a list like: 
<code>[140711676040768,140711676040769,140711676040770,140711676040771,....]
</code>
uses <code>ctypes.addressof(s.data[i])</code> that points to array element.


A:

The <code>_as_parameter_</code> of a ctypes pointer or array type is its address.  As an alternative to the format string, or using <code>id(s.data)</code>, you could do:
<code>&gt;&gt;&gt; import ctypes
&gt;&gt;&gt; class simple(ctypes.Structure):
...    _fields =
