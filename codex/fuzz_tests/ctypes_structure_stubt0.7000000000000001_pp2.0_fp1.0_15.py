import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char
    _fields_ = [("x", x), ("y", ctypes.c_int)]

ctypes.sizeof(S())
</code>
This raises a <code>TypeError</code> with the message
<code>TypeError: expected ctypes._SimpleCData, got ctypes.c_char
</code>
The error message is confusing because the message is talking about <code>ctypes.c_char</code> but the exception was raised when I was trying to create a field with <code>S.x</code> which is a <code>ctypes._SimpleCData</code>.
I understand why this exception is raised, but the error message is very confusing. Is there any reason why the error message is like this? Or is it a bug?

