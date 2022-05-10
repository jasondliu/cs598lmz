import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
</code>
Afterwards simply use this class for your model:
<code>class my_model(Model):
    data = model.Field(field_type=ctypes.CField)
</code>
Everything will be serialized correctly.
PS: <code>pytest</code> isn't the program who call this code (I tweaked my environment to call it nonetheless); the real problem is in the server, who call the request processors.

