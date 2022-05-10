import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class S2(ctypes.Structure):
    _fields_ = [('s1', S), ('s2', S)]

class Derived(S2):
    _fields_ = [('x', ctypes.c_int), ('s1', S)]

s = Derived()
print s.x
</code>


A:

You can kludge the behavior by assigning to <code>_fields_</code> after the class is defined. For example, replacing the last two lines of your program with
<code>class Derived(S2):
    _fields_ = [('x', ctypes.c_int), ('s1', S)]
Derived._fields_ = S2._fields_ + _fields_
s = Derived()
print s.x
</code>
prints <code>0</code> as I think you want. Note that this must be done with care. For example, if you replace the last line with <code>print s.s2.x</code>, the output is <code>0</code> instead of the expected <code>-142119
