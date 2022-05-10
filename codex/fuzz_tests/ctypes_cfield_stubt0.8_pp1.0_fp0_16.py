import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

print(ctypes.CField)
print(type(S.x))
print(S.x)
</code>
but it gives me an error:
<code>Traceback (most recent call last):
  File "C:\Users\Erik\workspaces\Python\Python_test\test.py", line 7, in &lt;module&gt;
    print(ctypes.CField)
AttributeError: type object 'ctypes.Structure' has no attribute 'CField'
</code>
where am I wrong?
I'm using Python 3.8.1 (and I see that in the documentation of ctypes there's not mentioned <code>CField</code> at all)
Thanks in advance


A:

<code>S.x</code> is not a <code>CField</code>, it's a <code>CField.type</code>, i.e. an instance of <code>CField</code>. If you want the class type, use:
<code>type(S.x)
</code>

