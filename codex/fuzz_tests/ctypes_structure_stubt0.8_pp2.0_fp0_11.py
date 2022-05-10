import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()

S._fields_ = [('x', ctypes.c_int)]
</code>
<code>$ python test_redefinition.py 
Traceback (most recent call last):
  File "test_redefinition.py", line 8, in &lt;module&gt;
    S._fields_ = [('x', ctypes.c_int)]
TypeError: _fields_ is final
</code>
Is there any way to get around this limitation? I am aware of the workaround involving creating a new class with the new definition, but I would prefer to avoid that if possible, because it requires some tricky imports.
EDIT: I created a new topic for the workaround that I had implemented.


A:

To avoid a new class, you could redefine the <code>_fields_</code> list in a class dictionary:
<code>S.__dict__['_fields_'] = [('x', ctypes.c_int)]
</code>
However, it doesn't seem to be a very good idea, because you will have to change all references to this attribute in
