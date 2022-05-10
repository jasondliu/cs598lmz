import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.Field = ctypes.CField
</code>
I'm getting the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib/python3.5/ctypes/__init__.py", line 669, in __getattr__
    func = self.__getitem__(name)
  File "/usr/lib/python3.5/ctypes/__init__.py", line 673, in __getitem__
    func = self._FuncPtr((name_or_ordinal, self))
AttributeError: type object 'CField' has no attribute '__getitem__'
</code>
What am I missing here?


A:

You need to add a <code>ctypes.POINTER</code> call to produce the a field descriptor. This is used to give details about the type that you want to create an array for.
I'm not sure about the point of this, exactly. 
<code>import ctypes


