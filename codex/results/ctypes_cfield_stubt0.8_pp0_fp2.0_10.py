import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
print 'Hello'
print ctypes.CField
</code>
This produces a <code>NameError</code>:
<code>Hello
Traceback (most recent call last):
  File "./c_field.py", line 8, in &lt;module&gt;
    print ctypes.CField
NameError: name 'ctypes' is not defined
</code>
Why is <code>CField</code> not defined?
If it's supposed to be defined, what am I doing wrong?

A similar script for <code>Structure</code> works well:
<code>import ctypes

class S(ctypes.Structure):
    pass

print S
</code>


A:

<code>ctypes</code> is a module, not a class.  You probably want:
<code>ctypes.CField = type(S.x)
print 'Hello'
print ctypes.CField
</code>

