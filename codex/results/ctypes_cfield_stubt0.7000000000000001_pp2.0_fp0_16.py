import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class A:
    pass

class B(A, ctypes.CField, ctypes.Structure):
    pass

b = B()
</code>
I get:
<code>Traceback (most recent call last):
  File "&lt;pyshell#12&gt;", line 1, in &lt;module&gt;
    b = B()
TypeError: Error when calling the metaclass bases
    metaclass conflict: the metaclass of a derived class must be a (non-strict) subclass of the metaclasses of all its bases
</code>
I don't understand this error message.  How can I fix it?
(The motivation for this is to make a subclass of <code>ctypes.Structure</code> that can be used as a <code>ctypes.CField</code> instance.)


A:

<code>ctypes.CField = type(S.x)
</code>
This sets <code>ctypes.CField</code> to be a <code>type</code> instance.  I'm guessing that <
