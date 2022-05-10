import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

print ctypes.CField
</code>
=> this gives me <code>&lt;class '_ctypes._CField_s'&gt;</code>

Now, I am doing this on python-2.6.6 on Linux and python-2.7.2 on Windows 7.
My problem is that I would like this to work on python-2.5.5 on a Solaris 10 machine but here when I do
<code>import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

print ctypes.CField
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "request-7.py", line 8, in &lt;module&gt;
    ctypes.CField = type(S.x)
ValueError: __class__ assignment: only for heap types
</code>
I don't know why this error is raised on python-2.5.5 on Solaris but
